def lib(a, b):
	c = 0
	i = 0
	while i < b:
		c += a
		i += 1
	return c

def loopmult75(x):
	if x >= 63 and x < 87:
		return lib(x, 75)
	return 0