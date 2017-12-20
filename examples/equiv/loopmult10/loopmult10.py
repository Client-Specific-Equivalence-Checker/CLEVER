def lib(a, b):
	c = 0
	i = 0
	while i < b:
		c += a
		i += 1
	return c

def loopmult10(x):
	if x >= 9 and x < 12:
		return lib(x,10)
	return 0
