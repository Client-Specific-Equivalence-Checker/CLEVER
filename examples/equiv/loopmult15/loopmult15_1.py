def lib(a, b):
	c = 0
	i = 0
	while i < a:
		c += b
		i += 1
	return c

def loopmult15(x):
	if x >= 13 and x < 16:
		return lib(x,15)
	return 0
