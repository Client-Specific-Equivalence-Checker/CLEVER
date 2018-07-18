def lib(x):
    counter = 0
    while x % 2 == 0:
        x = x//2
        counter+= 1
    return counter

def odd(x):
    if lib(x) == 0:
        return 1
    else:
        return 0
