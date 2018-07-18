def lib(a, b):
	c = 0
	if a < 0:
		i = 1
		while i <= a:
			c += b
			i += 1
	return c

def loopunreach100(x):                
	if x >= 85 and x < 115:                
		return lib(x, 100)                
	return 0
