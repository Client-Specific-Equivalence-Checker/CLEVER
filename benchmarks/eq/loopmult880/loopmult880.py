def lib(a, b):
	c = 0
	i = 0
	while i < b:
		c += a
		i += 1
	return c

def loopmult880(x):
	if x >= 833 and x < 927:
		return lib(x, 880)
	return 0