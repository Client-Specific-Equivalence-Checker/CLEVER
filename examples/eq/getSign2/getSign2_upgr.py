def lib(x):
    if x <= 0:
        return -1
    else:
        return 1

def get_sign2(x):
    if x > 0:
        return lib(x)
    return x