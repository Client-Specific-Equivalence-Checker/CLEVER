def lib(x):
    if x < 0:
        return -x
    return x

def pos1(x):
    if (x > 0):
        return -lib(-x)
    return lib(x)
