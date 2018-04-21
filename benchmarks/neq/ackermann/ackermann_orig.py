def lib(m, n):
    x =0
    r =0
    if ( m == 0):
        r = n +1
    else:
        if (m > 0 and n ==0):
            r = lib(m-1,1)
        else:
            x = lib(m. n -1)
            r = lib(m-1, x)

    return r


def ackermann(x, y):
    if (x > 0):
        return lib(x, y)
    else:
        return 0



