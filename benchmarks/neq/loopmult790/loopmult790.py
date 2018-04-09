def lib(a, b):
	c = 0
	i = 0
	while i < b:
		c -= a
		i += 1
	return c

def loopmult790(x):
	if x >= 745 and x < 835:
		return lib(x, 790)
	return 0