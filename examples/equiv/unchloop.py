from symbolic.args import *

def lib1(a, b):
    c = 1
    i = 0
    while i < a:
        c = c + b
        i += 1
    return c

def lib2(a, b):
    c = 0
    i = 0
    while i < a:
        c = c + b
        i += 1
    return c+1

@uninterp(lib=lambda *x : 0)
def unchloop(x):
    return lib(5,900)


def wrap(x, lib):
    return lib(5,900)

def check_counter(x):
  return (wrap(x, lib1), wrap(x, lib2))