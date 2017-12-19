from symbolic.args import *
primes = [ 2, 3, 5, 7, 11, 13, 17, 19 ]

def lib1(x, b):
  if (b == 0):
    return 0
  else:
    for p in primes:
      mod = x % p
      if (mod == 0):
        return 0
  return 1

def lib2(x, b):
  if (b == 0):
    return 0
  else:
    for p in primes:
      mod = x % p
      if (mod == 0):
        if x == p:
            return 1
        else:
            return 0
  return 1

@uninterp(lib=lambda x, y : x)
def is_prime3(x):
    for p in primes:
        if x == p:
            return 1
    return lib(x,1)

def wrap(x, lib):
    for p in primes:
        if x == p:
            return 1
    return lib(x,1)

def check_counter(x):
  return (wrap(x, lib1), wrap(x, lib2))