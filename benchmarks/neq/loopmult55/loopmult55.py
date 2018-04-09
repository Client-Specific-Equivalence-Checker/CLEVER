def lib(a, b):
	c = 0
	i = 0
	while i < b:
		c -= a
		i += 1
	return c

def loopmult55(x):
	if x >= 45 and x < 65:
		return lib(x, 55)
	return 0