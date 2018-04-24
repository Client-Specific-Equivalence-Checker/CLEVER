def lib(a, b):
	c = 0
	if a < 0:
		i = 1
		while i <= a:
			c += b
			i += 1
	return c

def loopunreach30(x):                
	if x >= 25 and x < 35:                
		return lib(x, 30)                
	return 0
