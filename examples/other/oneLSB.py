from symbolic.args import *

def lib1(x):
    # not a thing for ints in smt
    return x | 1

def lib2(x):
    return x + 1

@uninterp(lib=lambda x : x)
def oneLSB(x):
    if x % 2 == 0:
        return lib(x)
    else:
        return x
    return lib(x)

def wrap(x, lib):
    if x % 2 == 0:
        return lib(x)
    else:
        return x
    return lib(x)

def check_counter(x):
  return (wrap(x, lib1), wrap(x, lib2))