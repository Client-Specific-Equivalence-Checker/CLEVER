def lib(a, b):
	c = 0
	i = 0
	while i < a:
		c += b
		i += 1
	return c

def loopmult550(x):
	if x >= 513 and x < 587:
		return lib(x, 550)
	return 0