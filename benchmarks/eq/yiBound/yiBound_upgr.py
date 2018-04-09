def lib(x):
    if x > 10:
        return 12
    else:
        return x+1

def yiBound(x):
    if x < -100 or x > 100:
        return x
    if x > lib(x):
        return x
    else:
        return lib(x)
