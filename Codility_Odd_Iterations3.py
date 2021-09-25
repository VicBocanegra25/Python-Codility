def solution (A = list):
	"""A code that gives the unpaired value from an array"""
	result = 0
	count = 0
	for item in A:
		count = A.count(item)
		if count % 2 == 0:
			continue
		else:
			result = item
			break
	return result
if __name__ == '__main__':
	print(solution([1,2,1,5,5,2,2,3,7,7,3,1,2,1,1]))