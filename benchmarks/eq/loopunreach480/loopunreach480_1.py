def lib(a, b):
	c = 0
	if a < 0:
		i = 1
		while i <= a:
			c += b
			i += 1
	return c

def loopunreach480(x):                
	if x >= 445 and x < 515:                
		return lib(x, 480)                
	return 0
