# python3

def greedySum(L, s):
	""" input: s, positive integer, what the sum should add up to
			   L, list of unique positive integers sorted in descending order
		Use the greedy approach where you find the largest multiplier for 
		the largest value in L then for the second largest, and so on to 
		solve the equation s = L[0]*m_0 + L[1]*m_1 + ... + L[n-1]*m_(n-1)
		return: the sum of the multipliers or "no solution" if greedy approach does 
				not yield a set of multipliers such that the equation sums to 's'
	"""
	def find_largest_multiplier(largest_value, s):
		return int(s / largest_value)

	sum_of_multipliers = 0

	for i in range(len(L)):
		lm = find_largest_multiplier(L[i], s)
		sum_of_multipliers += lm
		s -= lm * L[i]

	if s == 0:
		return sum_of_multipliers
	else:
		return "no solution"

# For test purposes
if __name__ == '__main__':
	L = [10,9,8,7,6,5,4,3,2,1] 		# unique positive integers with n elements
	s = 34							# positive integer sum
	print(greedySum(L, s))