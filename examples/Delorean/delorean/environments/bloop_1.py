import decimal
import delorean.environments.datetime_1 as datetime

ENCODING = "utf-8"
STRING = "S"
NUMBER = "N"
BINARY = "B"
BOOLEAN = "BOOL"
MAP = "M"
LIST = "L"

PRIMITIVES = {"S", "N", "B"}
SETS = {"SS", "NS", "BS"}
DOCUMENTS = {"L", "M"}
ALL = {*PRIMITIVES, *SETS, *DOCUMENTS, BOOLEAN}

# Dynamo takes numbers as strings to reduce inter-language problems
DYNAMODB_CONTEXT = decimal.Context(
    Emin=-128, Emax=126, rounding=None, prec=38,
    traps=[
        decimal.Clamped, decimal.Overflow, decimal.Inexact,
        decimal.Rounded, decimal.Underflow
    ]
)

SUPPORTED_OPERATIONS = {
    "==": ALL,
    "!=": ALL,
    "<": PRIMITIVES,
    ">": PRIMITIVES,
    "<=": PRIMITIVES,
    ">=": PRIMITIVES,
    "begins_with": {STRING, BINARY},
    "between": PRIMITIVES,
    "contains": {*SETS, STRING, BINARY, LIST},
    "in": ALL
}


def supports_operation(operation, typedef):
    return typedef.backing_type in SUPPORTED_OPERATIONS[operation]


class Type:
    """Abstract base type."""

    python_type = None
    backing_type = None

    def __init__(self):
        if not hasattr(self, "inner_typedef"):
            self.inner_typedef = self
        super().__init__()

    def dynamo_dump(self, value, *, context, **kwargs):
        """Converts a local value into a DynamoDB value.
        For example, to store a string enum as an integer:
        .. code-block:: python
            def dynamo_dump(self, value, *, context, **kwargs):
                colors = ["red", "blue", "green"]
                return colors.index(value.lower())
        """
        raise NotImplementedError

    def dynamo_load(self, value, *, context, **kwargs):
        """Converts a DynamoDB value into a local value.
        For example, to load a string enum from an integer:
        .. code-block:: python
            def dynamo_dump(self, value, *, context, **kwargs):
                colors = ["red", "blue", "green"]
                return colors[value]
        """
        raise NotImplementedError

    def _dump(self, value, **kwargs):
        """Entry point for serializing values.  Most custom types should use :func:`~bloop.types.Type.dynamo_dump`.
        This wraps the return value of :func:`~bloop.types.Type.dynamo_dump` in DynamoDB's wire format.
        For example, serializing a string enum to an int:
        .. code-block:: python
            value = "green"
            # dynamo_dump("green") = 2
            _dump(value) == {"N": 2}
        If a complex type calls this function with ``None``, it will forward ``None`` to
        :func:`~bloop.types.Type.dynamo_dump`.  This can happen when dumping eg. a sparse
        :class:`~.bloop.types.Map`, or a missing (not set) value.
        """
        value = self.dynamo_dump(value, **kwargs)
        if value is None:
            return value
        return {self.backing_type: value}

    def _load(self, value, **kwargs):
        """Entry point for deserializing values.  Most custom types should use :func:`~bloop.types.Type.dynamo_load`.
        This unpacks DynamoDB's wire format and calls :func:`~bloop.types.Type.dynamo_load` on the inner value.
        For example, deserializing an int to a string enum:
        .. code-block:: python
            value = {"N": 2}
            # dynamo_load(2) = "green"
            _load(value) == "green"
        If a complex type calls this function with ``None``, it will forward ``None`` to
        :func:`~bloop.types.Type.dynamo_load`.  This can happen when loading eg. a sparse :class:`~bloop.types.Map`.
        """
        if value is not None:
            value = next(iter(value.values()))
        return self.dynamo_load(value, **kwargs)

    def __repr__(self):
        # Render class python types by name
        python_type = self.python_type
        if isinstance(python_type, type):
            python_type = python_type.__name__

        return "<{}[{}:{}]>".format(
            self.__class__.__name__,
            self.backing_type, python_type
        )


class String(Type):
    python_type = str
    backing_type = STRING

    def dynamo_load(self, value, *, context, **kwargs):
        return value

    def dynamo_dump(self, value, *, context, **kwargs):
        if value is None:
            return None
        return value


FIXED_ISO8601_FORMAT = "%Y-%m-%dT%H:%M:%S.%f+00:00"

class DateTime(String):
    """Always stored in DynamoDB using the :data:`~bloop.types.FIXED_ISO8601_FORMAT` format.
    Naive datetimes (``tzinfo is None``) are not supported, and trying to use one will raise ``ValueError``.
    .. code-block:: python
        from datetime import datetime, timedelta, timezone
        class Model(Base):
            id = Column(Integer, hash_key=True)
            date = Column(DateTime)
        engine.bind()
        obj = Model(id=1, date=datetime.now(timezone.utc))
        engine.save(obj)
        one_day_ago = datetime.now(timezone.utc) - timedelta(days=1)
        query = engine.query(
            Model,
            key=Model.id==1,
            filter=Model.date >= one_day_ago)
        query.first().date
    .. note::
        To use common datetime libraries such as `arrow`_, `delorean`_, or `pendulum`_,
        see :ref:`DateTime and Timestamp Extensions <user-extensions-datetime>` in the user guide.  These
        are drop-in replacements and support non-utc timezones:
        .. code-block:: python
            from bloop import DateTime  # becomes:
            from bloop.ext.pendulum import DateTime
    .. _arrow: http://crsmithdev.com/arrow
    .. _delorean: https://delorean.readthedocs.io/en/latest/
    .. _pendulum: https://pendulum.eustace.io
    """
    # python_type = datetime.datetime
    python_type = datetime.Datetime

    def dynamo_load(self, value, *, context, **kwargs):
        if value is None:
            return None
        # dt = datetime.datetime.strptime(value, FIXED_ISO8601_FORMAT)
        dt = datetime.Datetime.strptime(value, FIXED_ISO8601_FORMAT)
        # we assume all stored values are utc, so we simply force timezone to utc
        # without changing the day/time values
        # return dt.replace(tzinfo=datetime.timezone.utc)
        return dt.replace(tzinfo=datetime.utc)

    def dynamo_dump(self, value, *, context, **kwargs):
        if value is None:
            return None
        if value.tzinfo is None:
            raise ValueError(
                "naive datetime instances are not supported.  You can set a timezone with either "
                "your_dt.replace(tzinfo=) or your_dt.astimezone(tz=).  WARNING: calling astimezone on a naive "
                "datetime will assume the naive datetime is in the system's timezone, even though "
                "datetime.utcnow() creates a naive object!  You almost certainly don't want to do that."
            )
        # dt = value.astimezone(tz=datetime.timezone.utc)
        dt = value.astimezone(tz=datetime.utc)
        return dt.strftime(FIXED_ISO8601_FORMAT)
