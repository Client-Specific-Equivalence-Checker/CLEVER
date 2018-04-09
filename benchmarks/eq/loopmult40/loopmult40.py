def lib(a, b):
	c = 0
	i = 0
	while i < b:
		c += a
		i += 1
	return c

def loopmult40(x):
	if x >= 33 and x < 47:
		return lib(x, 40)
	return 0