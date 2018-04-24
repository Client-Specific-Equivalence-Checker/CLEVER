def lib(a, b):
	c = 1
	if b < 0:
		i = 1
		while i <= b:
			c += a
			i += 1
	return c

def loopunreach100(x):                
	if x >= 85 and x < 115:                
		return lib(x, 100)                
	return 0
