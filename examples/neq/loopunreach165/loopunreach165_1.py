def lib(a, b):
	c = 0
	if a < 0:
		i = 1
		while i <= a:
			c += b
			i += 1
	return c

def loopunreach165(x):                
	if x >= 145 and x < 185:                
		return lib(x, 165)                
	return 0
