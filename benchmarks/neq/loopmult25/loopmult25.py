def lib(a, b):
	c = 0
	i = 0
	while i < b:
		c -= a
		i += 1
	return c

def loopmult25(x):
	if x >= 23 and x < 27:
		return lib(x, 25)
	return 0