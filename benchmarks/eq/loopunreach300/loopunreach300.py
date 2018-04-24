def lib(a, b):
	c = 0
	if b < 0:
		i = 1
		while i <= b:
			c += a
			i += 1
	return c

def loopunreach300(x):                
	if x >= 273 and x < 327:                
		return lib(x, 300)                
	return 0
