def lib(a, b):
	c = 0
	if a < 0:
		i = 1
		while i <= a:
			c += b
			i += 1
	return c

def loopunreach625(x):                
	if x >= 585 and x < 665:                
		return lib(x, 625)                
	return 0
