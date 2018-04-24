def lib(a, b):
	c = 0
	if a < 0:
		i = 1
		while i <= a:
			c += b
			i += 1
	return c

def loopunreach550(x):                
	if x >= 513 and x < 587:                
		return lib(x, 550)                
	return 0
