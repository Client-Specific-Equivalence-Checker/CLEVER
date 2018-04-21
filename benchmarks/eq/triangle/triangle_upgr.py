def lib(n, s):
    r = 0
    if (n <= 0):
        r = s
    else:
        r = lib(n-1, n + s)
    return r

def triangle(n):
    r = lib(n, 0)
    return r
