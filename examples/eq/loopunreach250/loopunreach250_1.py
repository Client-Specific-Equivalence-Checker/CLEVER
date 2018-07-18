def lib(a, b):
	c = 0
	if a < 0:
		i = 1
		while i <= a:
			c += b
			i += 1
	return c

def loopunreach250(x):                
	if x >= 225 and x < 275:                
		return lib(x, 250)                
	return 0
