def loop_rec(m):
    if (m > 0):
        result = tr(m-1)
        result = result + m
    else:
        result = 0;

    return result

def tr(n):

    i = 0
    result = 0

    while (i < n):
        result = result + i

    return result
