from delorean.environments.datetime_1 import *
from delorean.clients.bii_server_1_new import *

###########################
# Wrapping Functions
###########################
def bii_1(year, month, day, hour, minute, second, tz):
    dt = Datetime(year, month, day, hour, minute, second, tz)
    utcdt = UtcDatetime(dt, tz)
    # this is how delorean checks if two delorean objects are equal.
    return utcdt._delorean.epoch
