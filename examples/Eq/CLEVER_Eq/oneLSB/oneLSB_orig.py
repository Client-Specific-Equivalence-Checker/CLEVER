def lib(x):
    return x | 1

def oneLSB(x):
    if x % 2 == 0:
        return lib(x)
    else:
        return x
    return lib(x)
