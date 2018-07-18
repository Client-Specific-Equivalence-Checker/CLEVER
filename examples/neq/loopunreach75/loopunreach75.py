def lib(a, b):
	c = 1
	if b < 0:
		i = 1
		while i <= b:
			c += a
			i += 1
	return c

def loopunreach75(x):                
	if x >= 63 and x < 87:                
		return lib(x, 75)                
	return 0
