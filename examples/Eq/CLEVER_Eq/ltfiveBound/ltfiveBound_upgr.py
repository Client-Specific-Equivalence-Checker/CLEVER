def lib(x):
    if x < 0:
        return 0
    else:
        return x

def ltfiveBound(x):
    if x < -100 or x > 100:
        return x
    if x < 0:
        return -lib((-x)*5)//5
    else:
        return lib((x+1)*5)//5 - 1
