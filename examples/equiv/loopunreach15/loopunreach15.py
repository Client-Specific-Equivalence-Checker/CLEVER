def lib(a, b):
    c=0
    if b < 0:
        i = 1
        while i <= b:
            c += a
            i += 1
    return c

def loopunreach15(x):
	if x >= 13 and x < 16:
		return lib(x,15)
	return 0
