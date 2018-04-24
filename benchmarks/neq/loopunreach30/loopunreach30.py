def lib(a, b):
	c = 1
	if b < 0:
		i = 1
		while i <= b:
			c += a
			i += 1
	return c

def loopunreach30(x):                
	if x >= 25 and x < 35:                
		return lib(x, 30)                
	return 0
