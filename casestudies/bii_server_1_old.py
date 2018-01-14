###########################
# INFO:
# '##' means original code commented out
###########################
UTC = 0
PST = 1
PST8PDT = 2
ALL_TIMEZONES = [UTC, PST, PST8PDT]

SECOND = 1

###########################
# MODELING ENVIRONEMNT
###########################
class datetime(object):
    def __init__(self, epoch, tz=0):
        self.epoch = epoch #seconds since start of time
        self.tz = tz
    
    @staticmethod
    def utcnow():
        return datetime(0)

class tzinfo(object):
    def __init__(self, tz):
        self.tz = tz

    def localize(self, datetime):
        datetime.tz = self.tz
        return datetime

    def normalize(self, datetime):
        datetime.tz = 0
        return datetime

class pytz(object):
    @staticmethod
    def timezone(tz):
        return tzinfo(tz)

###########################
# Wrapping Functions
###########################
def bii_server_1_old(epoch, tz):
    dt = datetime(epoch)
    utcdt = UtcDatetime(dt, tz)
    return utcdt._delorean.epoch # this is how delorean checks if two delorean objects are equal.


########################### 
# BII_SERVER CODE
# https://github.com/biicode/bii-server/blob/d2d7f2f0e38ff5ffdf1918ddeb33d1f4b1b530b1/model/epoch/utc_datetime.py
############################
class UtcDatetime(object):
    """Class for manage datetimes. The timezone is always internally in UTC. Its used for unify serialization
    and ease complexity of manage datetimes with timezones. Always use this class for datetime management"""

    def __init__(self, the_datetime, the_timezone):
        """the_datetime must be a datetime.datetime
           the_timezone is a String identifing timezone: EX: 'Europe/Madrid' 'UTC' See: all_timezones"""
        the_timezone = self._get_timezone_parameter(the_timezone)
        ## self._delorean = Delorean(datetime=the_datetime, timezone=the_timezone).shift("UTC")
        self._delorean = Delorean(datetime=the_datetime, timezone=the_timezone).shift(UTC)
        ## self._delorean.truncate('second')  # Truncate to second, its the precission of serialize
        self._delorean.truncate(SECOND)  # Truncate to second, its the precission of serialize

    @staticmethod
    def get_all_timezones():
        """All timezones available"""
        ## return all_timezones
        return ALL_TIMEZONES 

    def _get_timezone_parameter(self, the_timezone):
        """Gets a valid timezone parameter or raise"""
        ## if the_timezone == "PST":  # Very common
        if the_timezone == PST:  # Very common
        ##     return "PST8PDT"
            return PST8PDT
        if the_timezone not in self.get_all_timezones():
            raise ValueError("%s is not a valid timezone" % the_timezone)
        return the_timezone


############################################### 
# DELOREAN CODE
###############################################
from casestudies.delorean.exceptions import DeloreanInvalidTimezone

def get_total_second(td):
    """
    This method takes a timedelta and return the number of seconds it
    represents with the resolution of 10**6
    """
    return (td.microseconds + (td.seconds + td.days * 24 * 3600) * 1e6) / 1e6

def is_datetime_naive(dt):
    """
    This method returns true if the datetime is naive else returns false
    """
    if dt.tzinfo is None:
        return True
    else:
        return False

def is_datetime_instance(dt):
    if dt is None:
        return
    if not isinstance(dt, datetime):
        raise ValueError('Please provide a datetime instance to Delorean')

def datetime_timezone(tz):
    """
    This method given a timezone returns a localized datetime object.
    """
    utc_datetime_naive = datetime.utcnow()
    # return a localized datetime to UTC
    utc_localized_datetime = localize(utc_datetime_naive, 'UTC')
    # normalize the datetime to given timezone
    normalized_datetime = normalize(utc_localized_datetime, tz)
    return normalized_datetime

def localize(dt, tz):
    """
    Given a naive datetime object this method will return a localized
    datetime object
    """
    if not isinstance(tz, tzinfo):
        tz = pytz.timezone(tz)

    return tz.localize(dt)

def normalize(dt, tz):
    """
    Given a object with a timezone return a datetime object
    normalized to the proper timezone.
    This means take the give localized datetime and returns the
    datetime normalized to match the specificed timezone.
    """
    if not isinstance(tz, tzinfo):
        tz = pytz.timezone(tz)
    dt = tz.normalize(dt)
    return dt

class Delorean(object):
    """
    The class `Delorean <Delorean>` object. This method accepts naive
    datetime objects, with a string timezone.
    """
    _VALID_SHIFT_DIRECTIONS = ('last', 'next')
    _VALID_SHIFT_UNITS = ('second', 'minute', 'hour', 'day', 'week',
                          'month', 'year', 'monday', 'tuesday', 'wednesday',
                          'thursday', 'friday', 'saturday', 'sunday')

    def __init__(self, datetime=None, timezone=None):
        # maybe set timezone on the way in here. if here set it if not
        # use UTC
        is_datetime_instance(datetime)

        if datetime:
            if is_datetime_naive(datetime):
                if timezone:
                    if isinstance(timezone, tzoffset):
                        utcoffset = timezone.utcoffset(None)
                        total_seconds = (
                            (utcoffset.microseconds + (
                                utcoffset.seconds + utcoffset.days * 24 * 3600) * 10 ** 6) / 10 ** 6)
                        self._tzinfo = pytz.FixedOffset(total_seconds / 60)
                    elif isinstance(timezone, tzinfo):
                        self._tzinfo = timezone
                    else:
                        self._tzinfo = pytz.timezone(timezone)
                    self._dt = localize(datetime, self._tzinfo)
                    self._tzinfo = self._dt.tzinfo
                else:
                    # TODO(mlew, 2015-08-09):
                    # Should we really throw an error here, or should this 
                    # default to UTC?)
                    raise DeloreanInvalidTimezone('Provide a valid timezone')
            else:
                self._tzinfo = datetime.tzinfo
                self._dt = datetime
        else:
            if timezone:
                if isinstance(timezone, tzoffset):
                    self._tzinfo = pytz.FixedOffset(timezone.utcoffset(None).total_seconds() / 60)
                elif isinstance(timezone, tzinfo):
                    self._tzinfo = timezone
                else:
                    self._tzinfo = pytz.timezone(timezone)

                self._dt = datetime_timezone(self._tzinfo)
                self._tzinfo = self._dt.tzinfo
            else:
                self._tzinfo = pytz.utc
                self._dt = datetime_timezone('UTC')

    def shift(self, timezone):
        """
        Shifts the timezone from the current timezone to the specified timezone associated with the Delorean object,
        modifying the Delorean object and returning the modified object.
        .. testsetup::
            from datetime import datetime
            from delorean import Delorean
        .. doctest::
            >>> d = Delorean(datetime(2015, 1, 1), timezone='US/Pacific')
            >>> d.shift('UTC')
            Delorean(datetime=datetime.datetime(2015, 1, 1, 8, 0), timezone='UTC')
        """
        try:
            self._tzinfo = pytz.timezone(timezone)
        except pytz.UnknownTimeZoneError:
            raise DeloreanInvalidTimezone('Provide a valid timezone')
        self._dt = self._tzinfo.normalize(self._dt.astimezone(self._tzinfo))
        self._tzinfo = self._dt.tzinfo
        return self

    def truncate(self, s):
        """
        Truncate the delorian object to the nearest s
        (second, minute, hour, day, month, year)

        This is a destructive method, modifies the internal datetime
        object associated with the Delorean object.

        .. testsetup::

            from datetime import datetime
            from delorean import Delorean

        .. doctest::

            >>> d = Delorean(datetime(2015, 1, 1, 12, 10), timezone='US/Pacific')
            >>> d.truncate('hour')
            Delorean(datetime=datetime.datetime(2015, 1, 1, 12, 0), timezone='US/Pacific')

        """
        if s == 'second':
            self._dt = self._dt.replace(microsecond=0)
        elif s == 'minute':
            self._dt = self._dt.replace(second=0, microsecond=0)
        elif s == 'hour':
            self._dt = self._dt.replace(minute=0, second=0, microsecond=0)
        elif s == 'day':
            self._dt = self._dt.replace(hour=0, minute=0, second=0, microsecond=0)
        elif s == 'month':
            self._dt = self._dt.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
        elif s == 'year':
            self._dt = self._dt.replace(month=1, day=1, hour=0, minute=0, second=0, microsecond=0)
        else:
            raise ValueError("Invalid truncation level")

        return self

    @property
    def epoch(self):
        """
        Returns the total seconds since epoch associated with
        the Delorean object.

        .. testsetup::

            from datetime import datetime
            from delorean import Delorean

        .. doctest::

            >>> d = Delorean(datetime(2015, 1, 1), timezone='US/Pacific')
            >>> d.epoch
            1420099200.0

        """
        epoch_sec = pytz.utc.localize(datetime.utcfromtimestamp(0))
        now_sec = pytz.utc.normalize(self._dt)
        delta_sec = now_sec - epoch_sec
        return get_total_second(delta_sec)