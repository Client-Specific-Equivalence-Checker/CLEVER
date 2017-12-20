def lib(x):
    if x > 10:
        return 11
    else:
        return x

def yi1(x):
    if x > lib(x):
        return x
    else:
        return lib(x)
