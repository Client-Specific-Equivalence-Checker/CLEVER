
def lib(x):
    counter = 0
    while x < 0:
        x+=1
        counter+=1
    return counter

def pos2(x):
    if x > 0:
        return -lib(-x)
    else:
        return lib(x)
