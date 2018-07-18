def lib(a, b):
	c = 0
	if b < 0:
		i = 1
		while i <= b:
			c += a
			i += 1
	return c

def loopunreach40(x):                
	if x >= 33 and x < 47:                
		return lib(x, 40)                
	return 0
