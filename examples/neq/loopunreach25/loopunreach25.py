def lib(a, b):
	c = 1
	if b < 0:
		i = 1
		while i <= b:
			c += a
			i += 1
	return c

def loopunreach25(x):                
	if x >= 23 and x < 27:                
		return lib(x, 25)                
	return 0
