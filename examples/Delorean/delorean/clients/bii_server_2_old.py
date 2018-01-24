from delorean.libs.delorean_init_2_old import *
from delorean.environments.datetime_1 import *

########################### 
# BII_SERVER CODE (CLIENT)
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
