def lib(a, b):
	c = 0
	i = 0
	while i < b:
		c += a
		i += 1
	return c

def loopmult300(x):
	if x >= 273 and x < 327:
		return lib(x, 300)
	return 0