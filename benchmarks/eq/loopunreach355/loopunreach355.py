def lib(a, b):
	c = 0
	if b < 0:
		i = 1
		while i <= b:
			c += a
			i += 1
	return c

def loopunreach355(x):                
	if x >= 325 and x < 385:                
		return lib(x, 355)                
	return 0
