from delorean.clients.speculator_new_mod import *

def spec_2(year, month, day, direction, unit, count):
    ret = get_end_start_epochs(year, month, day, direction, unit, count)
    return ret['shifted']