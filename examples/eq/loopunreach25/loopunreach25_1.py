def lib(a, b):
	c = 0
	if a < 0:
		i = 1
		while i <= a:
			c += b
			i += 1
	return c

def loopunreach25(x):                
	if x >= 23 and x < 27:                
		return lib(x, 25)                
	return 0
