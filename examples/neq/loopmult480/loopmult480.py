def lib(a, b):
	c = 0
	i = 0
	while i < b:
		c -= a
		i += 1
	return c

def loopmult480(x):
	if x >= 445 and x < 515:
		return lib(x, 480)
	return 0