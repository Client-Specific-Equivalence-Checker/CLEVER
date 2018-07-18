def lib(a, b):
    c = 0
    i = 0
    while i < a:
        c = c + b
        i += 1
    return c+1

def unchloop(x):
    return lib(5,900)
