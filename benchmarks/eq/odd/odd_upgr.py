def lib(x):
    return (x+1) % 2

def odd(x):
    if lib(x) == 0:
        return 1
    else:
        return 0
