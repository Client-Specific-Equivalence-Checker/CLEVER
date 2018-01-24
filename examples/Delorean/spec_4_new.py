from delorean.clients.speculator_3_new import *

def spec_4(year, month, day, direction, unit, count):
    ret = get_end_start_epochs(year, month, day, direction, unit, count)
    return ret['shifted'] - ret['initial']