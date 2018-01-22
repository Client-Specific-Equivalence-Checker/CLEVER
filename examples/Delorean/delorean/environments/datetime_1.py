##############
# CONSTANTS
##############
NAIVE = -100
UTC = 0
PST = -7
PST8PDT = -7
ALL_TIMEZONES = list(range(-12, 15))

SECOND = 1


###########################
# MODELING ENVIRONEMNT
###########################
class Datetime(object):
    def __init__(self, year, month=1, day=1, hour=0, minute=0, second=0, tz=NAIVE):
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.second = second
        self.tzinfo = tz if isinstance(tz, Tzinfo) else Tzinfo(tz)
    
    @staticmethod
    def utcnow():
        return Datetime(0)

    def astimezone(self, tz):
        return Datetime(self.year, self.month, self.day, self.hour, self.minute, self.second, tz)

    @property
    def epoch(self):
        y = self.year * 360 * 24 * 60 * 60
        m = self.month * 30 * 24 * 60 * 60
        d = self.day * 24 * 60 * 60
        h = self.hour * 60 * 60
        mi = self.minute * 60
        s = self.second
        return y + m + d + h + mi + s + (self.tzinfo.tzinfo*60*60)

class Tzinfo(object):
    def __init__(self, tz):
        self.tzinfo = tz

    def localize(self, dt):
        dt.tz = self.tzinfo
        return dt

    def normalize(self, dt):
        dt.tz = 0
        return dt

class Tzoffset(object):
    pass

class Pytz(object):
    @staticmethod
    def timezone(tz):
        return Tzinfo(tz)

    @staticmethod
    def FixedOffset(offset):
        return Tzinfo(0)

    @staticmethod
    def utc():
        return Tzinfo(0)

###############################################
# DELOREAN CODE
###############################################
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
    # if dt.tzinfo is None:
    if dt.tzinfo.tzinfo == NAIVE:
        return True
    else:
        return False


def is_datetime_instance(dt):
    if dt is None:
        return
    if not isinstance(dt, Datetime):
        raise ValueError('Please provide a datetime instance to Delorean')


def datetime_timezone(tz):
    """
    This method given a timezone returns a localized datetime object.
    """
    utc_datetime_naive = Datetime.utcnow()
    # return a localized datetime to UTC
    # utc_localized_datetime = localize(utc_datetime_naive, 'UTC')
    utc_localized_datetime = localize(utc_datetime_naive, UTC)
    # normalize the datetime to given timezone
    normalized_datetime = normalize(utc_localized_datetime, tz)
    return normalized_datetime


def localize(dt, tz):
    """
    Given a naive datetime object this method will return a localized
    datetime object
    """
    if not isinstance(tz, Tzinfo):
        tz = Pytz.timezone(tz)

    return tz.localize(dt)


def normalize(dt, tz):
    """
    Given a object with a timezone return a datetime object
    normalized to the proper timezone.
    This means take the give localized datetime and returns the
    datetime normalized to match the specificed timezone.
    """
    if not isinstance(tz, Tzinfo):
        tz = Pytz.timezone(tz)
    dt = tz.normalize(dt)
    return dt
