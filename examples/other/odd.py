from symbolic.args import *

def lib1(x):
    counter = 0
    while x % 2 == 0:
        x = x//2
        counter+= 1
    return counter

def lib2(x):
    return (x+1) % 2

@uninterp(lib=lambda x : x)
def odd(x):
    if lib(x) == 0:
        return 1
    else:
        return 0

def wrap(x, lib):
    if lib(x) == 0:
        return 1
    else:
        return 0

def check_counter(x):
  return (wrap(x, lib1), wrap(x, lib2))