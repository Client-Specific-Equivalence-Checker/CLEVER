def lib(a, b):
	c = 0
	if a < 0:
		i = 1
		while i <= a:
			c += b
			i += 1
	return c

def loopunreach790(x):                
	if x >= 745 and x < 835:                
		return lib(x, 790)                
	return 0
