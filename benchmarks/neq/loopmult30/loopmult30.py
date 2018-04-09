def lib(a, b):
	c = 0
	i = 0
	while i < b:
		c -= a
		i += 1
	return c

def loopmult30(x):
	if x >= 25 and x < 35:
		return lib(x, 30)
	return 0