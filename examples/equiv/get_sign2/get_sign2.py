def lib(x):
    if x == 0:
        return 0
    elif x < 0:
        return -1
    else:
        return 1

def get_sign2(x):
    if lib(x) > 0:
        return 1
    return 0
