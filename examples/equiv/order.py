from symbolic.args import *

def lib1(x,y):
    return x - y

def lib2(x,y):
    if (x < y):
        temp = x
        x = y
        y = temp
    return (x - y)

@uninterp(lib=lambda x, y : x)
def order(c, d):
    if (c > d):
        return lib(c, d)
    return lib(d, c)


def wrap(c, d, lib):
    if (c > d):
        return lib(c, d)
    return lib(d, c)

def check_counter(c,d):
  return (wrap(c, d, lib1), wrap(c, d, lib2))