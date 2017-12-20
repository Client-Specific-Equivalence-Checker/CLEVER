def lib(a, b):
    c=0
    if a < 0:
        i = 1
        while i <= a:
            c += b
            i += 1
    return c

def loopunreach2(x):
    return lib(2,2)
