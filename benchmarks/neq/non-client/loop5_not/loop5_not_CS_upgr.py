def lib(n):
    i =n+1
    j =0
    while ( i > 0 ):
        j = j +2
        i = i -1
    return j


def loop5_not(x):
    if (x > 100 and x < 102):
        return lib(x)
    else:
        return 100

