def solution (A = list):
	"""A code that gives the unpaired value from an array"""
	new_array = [0] * (max(A)+1)
	position_of_impair = 0
	result = 0
	for item in A:
		new_array[item] = A.count(item) % 2
	position_of_impair = new_array.index(max(new_array))
	return position_of_impair
if __name__ == '__main__':
	print(solution([1,5,5,1,7,9,9,7,5,4,4,6,6]))
# dict = {0 : 2, 2: 1}
# #los valores 1, 2, 3, 5 serán índices del segundo array.
# b[1] = 2 % 2 = 0
# b[2] = 3 % 2 = 1 <- return índice
# b[3] = 0
# b[4] = 2
# b[5] = 2
#ele ementos dA son positivos (utilizar como índices)

#New array = [0, 2, 3, 0, 2, 2, 0, 2]
