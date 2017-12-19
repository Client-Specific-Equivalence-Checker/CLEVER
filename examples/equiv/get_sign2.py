from symbolic.args import *

def lib1(x):
    if x == 0:
        return 0
    elif x < 0:
        return -1
    else:
        return 1

def lib2(x):
    if x <= 0:
        return -1
    else:
        return 1

@uninterp(lib=lambda x : x)
def get_sign2(x):
    if lib(x) > 0:
        return 1
    return 0


def wrap(x, lib):
    if lib(x) > 0:
        return 1
    return 0

def check_counter(x):
  return (wrap(x, lib1), wrap(x, lib2))