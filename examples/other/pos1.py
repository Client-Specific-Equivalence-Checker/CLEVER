from symbolic.args import *

def lib1(x):
    #since counter is never made symbolic
    #the summary is not what you'd expect.
    counter = 0
    while x < 0:
        x += 1
        counter += 1
    return counter

def lib2(x):
    if x < 0:
        return -x
    return x

@uninterp(lib=lambda x : x)
def pos1(x):
    if (x > 0):
        return -lib(-x)
    return lib(x)


def wrap(x, lib):
    if (x > 0):
        return -lib(-x)
    return lib(x)

def check_counter(x):
  return (wrap(x, lib1), wrap(x, lib2))