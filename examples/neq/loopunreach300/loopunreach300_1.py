def lib(a, b):
	c = 0
	if a < 0:
		i = 1
		while i <= a:
			c += b
			i += 1
	return c

def loopunreach300(x):                
	if x >= 273 and x < 327:                
		return lib(x, 300)                
	return 0
