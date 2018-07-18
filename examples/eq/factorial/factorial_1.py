def lib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n * lib(n-1)


def factorial(x):
    if x < 5:
        return lib(x)
    else:
        return 0
