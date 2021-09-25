def solution (A = list):
	"""A code that gives the unpaired value from an array"""
	result = 0
	count = 1
	A.sort()
	A.append(max(A)+1)
	if len(A) == 1:
		return A[0]
	for index, item in enumerate(A):
		if item == A[index+1]:
			count += 1
		else:
			if count % 2 == 0:
				count = 1
			else:
				return item
	return resultÑ
if __name__ == '__main__':
	print(solution([1,1,1,2,5,2,5,1,9,15,9]))