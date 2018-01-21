###########################
# MODELING ENVIRONEMNT
###########################
class datetime(object):
    def __init__(self, epoch, tz=0):
        self.epoch = epoch #seconds since start of time
        self.tzinfo = tz
    
    @staticmethod
    def utcnow():
        return datetime(0)

    def astimezone(self, tzinfo):
        return datetime(0, tzinfo.tzinfo)

class tzinfo(object):
    def __init__(self, tz):
        self.tzinfo = tz

    def localize(self, datetime):
        datetime.tz = self.tzinfo
        return datetime

    def normalize(self, datetime):
        datetime.tz = 0
        return datetime

class tzoffset(object):
    pass

class pytz(object):
    @staticmethod
    def timezone(tz):
        return tzinfo(tz)

    @staticmethod
    def FixedOffset(offset):
        return tzinfo(0)

    @staticmethod
    def utc():
        return tzinfo(0)