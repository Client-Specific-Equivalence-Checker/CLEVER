from delorean.environments.datetime_1 import *
import delorean.environments.bloop_1 as types
import delorean.libs.delorean_init_new as delorean

DEFAULT_TIMEZONE = "utc"


class DateTime(types.DateTime):
    python_type = delorean.Delorean

    def __init__(self, timezone=DEFAULT_TIMEZONE):
        self.timezone = timezone
        super().__init__()

    def dynamo_dump(self, value, *, context, **kwargs):
        if value is None:
            return None
        value = value.shift("utc").datetime
        return super().dynamo_dump(value, context=context, **kwargs)

    def dynamo_load(self, value, *, context, **kwargs):
        if value is None:
            return None
        dt = super().dynamo_load(value, context=context, **kwargs)
        return delorean.Delorean(dt).shift(self.timezone)
