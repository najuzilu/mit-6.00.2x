# python3

def max_contig_sum(L):
	""" L, a list of integers, at least one positive
	Returns the maximum sum of a contiguous subsequence in L """
	
	def sum_window(rightBound, L, maxSum):
		subarrayMax.append(maxSum)
		if rightBound == len(L):
			return maxSum
		maxSum += L[rightBound]
		sum_window(rightBound + 1, L, maxSum)

	leftBound = 0
	array = []
	while leftBound <= len(L):
		global subarrayMax
		subarrayMax = []
		sum_window(leftBound, L, 0)
		array.append(max(subarrayMax))
		leftBound += 1
	return max(array)

# For test purposes
if __name__ == '__main__':
	L = [3, 4, -1, 5, -4]
	print(max_contig_sum(L))
	L = [3, 4, -8, 15, -1, 2]
	print(max_contig_sum(L))