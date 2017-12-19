from symbolic.args import *

def lib1(x):
    return x % 5

def lib2(x):
    return x % 6

@uninterp(lib=lambda x : x)
def multiple(x):
    x = x*5*6
    if lib(x) == 0:
        return 1
    else:
        return 0

def wrap(x, lib):
    x = x*5*6
    if lib(x) == 0:
        return 1
    else:
        return 0

def check_counter(x):
  return (wrap(x, lib1), wrap(x, lib2))