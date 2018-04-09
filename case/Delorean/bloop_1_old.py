from delorean.clients.bloop_1_new import *

###########################
# Wrapping Functions
###########################
def bloop_1(value):
    dt = DateTime()
    dt = dt.dynamo_load(value, context=None)
    return dt.epoch

print(bloop_1(1))