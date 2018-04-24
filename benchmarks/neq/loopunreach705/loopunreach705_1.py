def lib(a, b):
	c = 0
	if a < 0:
		i = 1
		while i <= a:
			c += b
			i += 1
	return c

def loopunreach705(x):                
	if x >= 663 and x < 747:                
		return lib(x, 705)                
	return 0
