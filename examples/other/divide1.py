from symbolic.args import *

def lib1(x,y):
    return x / y

def lib2(x, y):
    if (y == 0):
        return 0
    return x / y

@uninterp(lib=lambda x, y : x)
def divide1(c, d):
    if (d == 0):
        return 0
    return lib(c, d)


def wrap(c, d, lib):
    if (d == 0):
        return 0
    return lib(c, d)

def check_counter(c,d):
  return (wrap(c, d, lib1), wrap(c, d, lib2))