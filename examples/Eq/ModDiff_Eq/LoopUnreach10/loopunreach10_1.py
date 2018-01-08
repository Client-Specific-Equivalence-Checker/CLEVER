def lib(a, b):
    c=0
    if a < 0:
        i = 1
        while i <= a:
            c += b
            i += 1
    return c

def loopunreach10(x):
	if x >= 9 and x < 12:
		return lib(x,10)
	return 0
