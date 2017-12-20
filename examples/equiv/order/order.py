def lib(x,y):
    return x - y

def order(c, d):
    if (c > d):
        return lib(c, d)
    return lib(d, c)
