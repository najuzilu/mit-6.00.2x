import itertools
import numpy as np

def find_combination(choices, total):
	"""
	choices: a non-empty list of ints
	total: a positive int
 
	Returns result, a numpy.array of length len(choices) 
	such that
		* each element of result is 0 or 1
		* sum(result*choices) == total
		* sum(result) is as small as possible
	In case of ties, returns any result that works.
	If there is no result that gives the exact total, 
	pick the one that gives sum(result*choices) closest 
	to total without going over.
	"""
	power_set = []
	for i in itertools.product([1,0], repeat = len(choices)):
		power_set.append(np.array(i))
	filter_set_eq = []
	filter_set_less = []
	for j in power_set:
		if sum(j*choices) == total:
			filter_set_eq.append(j)
		elif sum(j*choices) < total:
			filter_set_less.append(j)
	if len(filter_set_eq) > 0:
		minidx = min(enumerate(filter_set_eq), key=lambda x:sum(x[1]))[1]
		return minidx
	else:
		minidx = max(enumerate(filter_set_less), key = lambda x:sum(x[1]))[1]
		return minidx

choices = [1,2,2,3]
total = 4
print(find_combination(choices, total))

choices = [1,1,3,5,3]
total = 5
print(find_combination(choices, total))

choices = [1,1,1,9]
total = 4
print(find_combination(choices, total))