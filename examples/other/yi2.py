from symbolic.args import *

def lib1(x):
    if x > 10:
        return 11
    else:
        return x

def lib2(x):
    if x > 11:
        return 11
    else:
        return x-1

@uninterp(lib=lambda x : x)
def yi2(x):
    if x > lib(x):
        return x
    else:
        return lib(x)

def wrap(x, lib):
    if x > lib(x):
        return x
    else:
        return lib(x)

def check_counter(x):
  return (wrap(x, lib1), wrap(x, lib2))