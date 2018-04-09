def lib(x):
    if x > 11:
        return 11
    else:
        return x-1

def yi2(x):
    if x > lib(x):
        return x
    else:
        return lib(x)

