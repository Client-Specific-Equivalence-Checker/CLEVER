def lib(a, b):
	c = 1
	if b < 0:
		i = 1
		while i <= b:
			c += a
			i += 1
	return c

def loopunreach415(x):                
	if x >= 383 and x < 447:                
		return lib(x, 415)                
	return 0
