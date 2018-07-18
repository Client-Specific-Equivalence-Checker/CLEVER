def lib(a, b):
	c = 0
	i = 0
	while i < a:
		c += b
		i += 1
	return c

def loopmult355(x):
	if x >= 325 and x < 385:
		return lib(x, 355)
	return 0