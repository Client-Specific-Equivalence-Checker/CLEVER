def lib(n):
    s = 0
    r = 0
    if (n <= 0):
        r = s
    else:
        r = lib(n-1, n + s)
    return r

def triangle(n):
    return lib(n)

