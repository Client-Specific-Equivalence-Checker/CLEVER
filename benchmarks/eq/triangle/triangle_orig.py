def lib(n):
    r = 0
    if (n <= 0):
        r = 0
    else:
        r = lib(n-1)
        r = n + r

    return r

def triangle(n):
    r = lib(n)
    return r