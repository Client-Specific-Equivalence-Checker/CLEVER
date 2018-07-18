def lib(a, b):
	c = 0
	if b < 0:
		i = 1
		while i <= b:
			c += a
			i += 1
	return c

def loopunreach130(x):                
	if x >= 113 and x < 147:                
		return lib(x, 130)                
	return 0
