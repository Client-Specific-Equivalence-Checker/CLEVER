def lib(a, b):
	c = 0
	i = 0
	while i < b:
		c -= a
		i += 1
	return c

def loopmult250(x):
	if x >= 225 and x < 275:
		return lib(x, 250)
	return 0