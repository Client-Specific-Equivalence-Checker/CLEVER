from symbolic.args import *

def lib1(a, b):
	c=a+b;
	return c+3;

def lib2(a, b):
	d=3;
	c=b+a;
	return c+d;

@uninterp(lib=lambda *x : 0)
def const(x):
    return lib(5,900)


def wrap(x, lib):
    return lib(5,900)

def check_counter(x):
  return (wrap(x, lib1), wrap(x, lib2))