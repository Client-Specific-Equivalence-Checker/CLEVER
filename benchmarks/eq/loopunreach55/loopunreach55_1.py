def lib(a, b):
	c = 0
	if a < 0:
		i = 1
		while i <= a:
			c += b
			i += 1
	return c

def loopunreach55(x):                
	if x >= 45 and x < 65:                
		return lib(x, 55)                
	return 0
