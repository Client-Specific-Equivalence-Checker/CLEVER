
def lib(x):
	if x < 0:
		return -x
	else:
		while x >= 0:
			x = x
		return x

def pos2(x):
    if x > 0:
        return -lib(-x)
    else:
        return lib(x)
