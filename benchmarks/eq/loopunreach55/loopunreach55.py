def lib(a, b):
	c = 0
	if b < 0:
		i = 1
		while i <= b:
			c += a
			i += 1
	return c

def loopunreach55(x):                
	if x >= 45 and x < 65:                
		return lib(x, 55)                
	return 0
