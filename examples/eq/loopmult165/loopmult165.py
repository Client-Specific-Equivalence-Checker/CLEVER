def lib(a, b):
	c = 0
	i = 0
	while i < b:
		c += a
		i += 1
	return c

def loopmult165(x):
	if x >= 145 and x < 185:
		return lib(x, 165)
	return 0