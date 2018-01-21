from delorean_case_study.environment import *

UTC = 0
PST = 1
PST8PDT = 2
ALL_TIMEZONES = [UTC, PST, PST8PDT]

SECOND = 1


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