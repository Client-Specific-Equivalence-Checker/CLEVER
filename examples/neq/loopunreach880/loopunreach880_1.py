def lib(a, b):
	c = 0
	if a < 0:
		i = 1
		while i <= a:
			c += b
			i += 1
	return c

def loopunreach880(x):                
	if x >= 833 and x < 927:                
		return lib(x, 880)                
	return 0
