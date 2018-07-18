def lib(x):
    return x % 6

def multipleBound(x):
    if x < -100 or x > 100:
        return x
    x = x*5*6
    if lib(x) == 0:
        return 1
    else:
        return 0
