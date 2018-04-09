primes = [ 2, 3, 5, 7, 11, 13, 17, 19 ]

def lib(x, b):
  if (b == 0):
    return 0
  else:
    for p in primes:
      mod = x % p
      if (mod == 0):
        return 0
  return 1

def is_prime1(x):
    return lib(x, 0)
