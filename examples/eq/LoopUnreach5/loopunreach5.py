def lib(a, b):
    c=0
    if b < 0:
        i = 1
        while i <= b:
            c += a
            i += 1
    return c

def loopunreach5(x):
	if x >= 5 and x < 7:
		return lib(x,5)
	return 0
