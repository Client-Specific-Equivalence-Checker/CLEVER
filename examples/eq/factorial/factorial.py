def lib(n):
    """Compute n! where n is an integer >= 0."""
    if n > 0:
        acc = 1
        x = 1
        while x < n + 1:
            acc *= x
            x +=1
        return acc
    return 0


def factorial(x):
    if x < 5:
        return lib(x)
    else:
        return 0
