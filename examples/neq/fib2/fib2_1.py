def lib(n):
    """ Imperative definition of Fibonacci numbers """
    a, b = 0, 1
    i = 0
    while(i < n):
        i += 1
        a, b = b, a + b
    return a

def fib2(x):
    if x < 5:
        return lib(x)
    else:
        return 0
