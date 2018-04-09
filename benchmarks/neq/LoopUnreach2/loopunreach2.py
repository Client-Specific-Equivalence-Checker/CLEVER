def lib(a, b):
    c=1
    if b < 0:
        i = 1
        while i <= b:
            c += a
            i += 1
    return c

def loopunreach2(x):
    return lib(2,2)
