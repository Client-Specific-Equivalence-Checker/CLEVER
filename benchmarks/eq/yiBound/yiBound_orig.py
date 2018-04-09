def lib(x):
    if x > 10:
        return 11
    else:
        return x

def yiBound(x):
    if x < -100 or x > 100:
        return x
    if x > lib(x):
        return x
    else:
        return lib(x)
