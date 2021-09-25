def solution(A):
	"""An program that finds the missing element from an array"""
	#Algoritmo:
	#sort the list
	#loop through each item, find if the value from next one is the same as the
	# current + 1. If it's not, then the missing item is current + 1
	# return result
	new_A = [0]
	result = 0
	if not A:
		return 1
	new_A = sorted(A)
	for index, item in enumerate (new_A):
		if item == max(new_A):
			return 1
		if item + 1 == new_A[index + 1]:
			continue
		else:
			result = item + 1
			return result
	return result

if __name__ == '__main__':
	print(solution([1]))