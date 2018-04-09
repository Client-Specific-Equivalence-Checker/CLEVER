def lib(a, b):
	c = 0
	i = 0
	while i < b:
		c -= a
		i += 1
	return c

def loopmult415(x):
	if x >= 383 and x < 447:
		return lib(x, 415)
	return 0