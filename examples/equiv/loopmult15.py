from symbolic.args import *

def lib1(a, b):
	c = 0
	i = 0
	while i < b:
		c += a
		i += 1
	return c

def lib2(a, b):
	c = 0
	i = 0
	while i < a:
		c += b
		i += 1
	return c

@uninterp(lib=lambda *x : 0)
def loopmult15(x):
	if x >= 13 and x < 16:
		return lib(x,15)
	return 0

def wrap(x, lib):
	if x >= 13 and x < 16:
		return lib(x,15)
	return 0

def check_counter(x):
  return (wrap(x, lib1), wrap(x, lib2))