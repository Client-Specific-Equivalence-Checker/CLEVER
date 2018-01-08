def lib(a, b):
	c = 0
	i = 0
	while i < b:
		c += a
		i += 1
	return c

def loopmult20(x):
	if x >= 18 and x < 22:
		return lib(x,20)
	return 0
