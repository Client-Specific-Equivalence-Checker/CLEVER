def lib(a, b):
	c = 0
	i = 0
	while i < b:
		c -= a
		i += 1
	return c

def loopmult205(x):
	if x >= 183 and x < 227:
		return lib(x, 205)
	return 0