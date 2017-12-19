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
def get_sign(x):
    return lib(x)


def wrap(x, lib):
    return lib(x)

def check_counter(x):
  return (wrap(x, lib1), wrap(x, lib2))