def stdDevOfLengths(L):
	"""
	L: a list of strings

	returns: float, the standard deviation of the lengths of the strings,
	  or NaN if L is empty.
	"""
	if len(L) == 0:
		return float('NaN')

	mean = len(''.join(L)) / len(L)
	std = 0.0 

	for x in L:
		std += (len(x) - mean)**2

	return (std / len(L))**0.5

# TEST CASES
L = ['a', 'z', 'p'] # should return 0
print('Should return 0')
print(stdDevOfLengths(L))

L = ['apples', 'oranges', 'kiwis', 'pineapples'] # should return 1.8708
print('Should return 1.8708')
print(stdDevOfLengths(L))