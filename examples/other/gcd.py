from symbolic.args import *

def lib1(a, b):
    if a < b:
        temp = a
        a = b
        b = temp
    r = a % b
    while r != 0:
        a = b
        b = r
        r = a % b
    return b

def lib2(a, b):
    if a < b:
        temp = a
        a = b
        b = temp

    if b == 0:
        return a

    r = a % b
    while r != 0:
        a = b
        b = r
        r = a % b
    return b

CDCE925_PLL_FREQUENCY_MIN = 80000
CDCE925_PLL_FREQUENCY_MAX = 230000

@uninterp(lib=lambda *x : 0)
def gcd(rate, parent_rate, n, m):
    if rate <= parent_rate:
        rate = parent_rate
        n = 0
        m = 0
        return 0
    else:
        if rate < CDCE925_PLL_FREQUENCY_MIN:
            rate = CDCE925_PLL_FREQUENCY_MIN
        elif rate > CDCE925_PLL_FREQUENCY_MAX:
            rate = CDCE925_PLL_FREQUENCY_MAX
        g = lib(rate, parent_rate)
        um = parent_rate // g
        un = rate // g
        
        while un > 4095 or um > 511:
            un = un >> 1
            um = um >> 1
        if un == 0:
            un = 1
        if um == 0:
            um = 1
        
        n = un
        m = um

        return g

def wrap(rate, parent_rate, n, m, lib):
    if rate <= parent_rate:
        rate = parent_rate
        n = 0
        m = 0
        return 0
    else:
        if rate < CDCE925_PLL_FREQUENCY_MIN:
            rate = CDCE925_PLL_FREQUENCY_MIN
        elif rate > CDCE925_PLL_FREQUENCY_MAX:
            rate = CDCE925_PLL_FREQUENCY_MAX
        g = lib(rate, parent_rate)
        um = parent_rate // g
        un = rate // g
        
        while un > 4095 or um > 511:
            un = un >> 1
            um = um >> 1
        if un == 0:
            un = 1
        if um == 0:
            um = 1
        
        n = un
        m = um

        return g

def check_counter(rate, parent_rate, n, m):
  return (wrap(rate, parent_rate, n, m, lib1), wrap(rate, parent_rate, n, m, lib2))