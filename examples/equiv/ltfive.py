from symbolic.args import *

def lib1(x):
    if x < 5:
        return 5
    else:
        return x

def lib2(x):
    if x < 0:
        return 0
    else:
        return x

@uninterp(lib=lambda x : x)
def ltfive(x):
    if x < 0:
        return -lib((-x)*5)//5
    else:
        return lib((x+1)*5)//5 - 1

def wrap(x, lib):
    if x < 0:
        return -lib((-x)*5)//5
    else:
        return lib((x+1)*5)//5 - 1

def check_counter(x):
  return (wrap(x, lib1), wrap(x, lib2))