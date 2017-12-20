def lib(a, b):
    c = 1
    i = 0
    while i < a:
        c = c + b
        i += 1
    return c

def unchloop(x):
    return lib(5,900)
