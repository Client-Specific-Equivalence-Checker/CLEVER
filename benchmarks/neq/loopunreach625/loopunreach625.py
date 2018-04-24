def lib(a, b):
	c = 1
	if b < 0:
		i = 1
		while i <= b:
			c += a
			i += 1
	return c

def loopunreach625(x):                
	if x >= 585 and x < 665:                
		return lib(x, 625)                
	return 0
