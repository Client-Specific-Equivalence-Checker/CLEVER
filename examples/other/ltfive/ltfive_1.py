def lib(x):
    if x < 0:
        return 0
    else:
        return x

def ltfive(x):
    if x < 0:
        return -lib((-x)*5)//5
    else:
        return lib((x+1)*5)//5 - 1

