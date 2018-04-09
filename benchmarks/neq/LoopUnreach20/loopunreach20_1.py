def lib(a, b):
    c=0
    if a < 0:
        i = 1
        while i <= a:
            c += b
            i += 1
    return c

def loopunreach20(x):
	if x >= 18 and x < 22:
		return lib(x,20)
	return 0
