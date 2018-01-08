def lib(x,y):
    if (x < y):
        temp = x
        x = y
        y = temp
    return (x - y)

def order(c, d):
    if (c > d):
        return lib(c, d)
    return lib(d, c)
