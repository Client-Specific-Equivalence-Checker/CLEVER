# This is intuitive but VERY slow
def lib(n):
    """ Functional definition of Fibonacci numbers """
    if n <= 1:
        return 0
    else:
        return lib(n - 1) + lib(n - 2)

def fib2(x):
    if x < 5:
        return lib(x)
    else:
        return 0
