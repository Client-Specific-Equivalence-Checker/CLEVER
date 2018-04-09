def lib(a, b):
	c = 0
	i = 0
	while i < b:
		c -= a
		i += 1
	return c

def loopmult100(x):
	if x >= 85 and x < 115:
		return lib(x, 100)
	return 0