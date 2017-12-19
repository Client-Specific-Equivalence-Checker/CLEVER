from symbolic.args import *

def lib1(a, b):
    c = b + a
    return c

def lib2(a, b):
    c = a + b
    return c

@uninterp(lib=lambda *x : 0)
def add(x):
    return lib(5,900)


def wrap(x, lib):
    return lib(5,900)

def check_counter(x):
  return (wrap(x, lib1), wrap(x, lib2))