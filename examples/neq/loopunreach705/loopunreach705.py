def lib(a, b):
	c = 1
	if b < 0:
		i = 1
		while i <= b:
			c += a
			i += 1
	return c

def loopunreach705(x):                
	if x >= 663 and x < 747:                
		return lib(x, 705)                
	return 0
