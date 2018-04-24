def lib(a, b):
	c = 1
	if b < 0:
		i = 1
		while i <= b:
			c += a
			i += 1
	return c

def loopunreach480(x):                
	if x >= 445 and x < 515:                
		return lib(x, 480)                
	return 0
