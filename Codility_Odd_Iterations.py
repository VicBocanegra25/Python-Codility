def solution (A = list):
	"""A code that gives the unpaired value from an array"""
	result = 0
	second_array = [0] * len(A)
	# start a flag
	# loop over all items of the array, count them.
	# if result not even, return result
	current = 0
	while True:
		temp = A.count(A[current])
		if (temp % 2) == 0:
			current += 1
			continue
		else:
			result = A[current]
			break
	return result

	#conteo dinámico
	#meta: leer una sola vez A y poner en otro array
	#¿Qué valores se almacenan en el otro array? ¿para qué?
	#El otro array será el conteo


if __name__ == '__main__':
	print(solution([1, 2, 1, 4, 4, 5, 2 ,2, 5, 7, 7]))
# dict = {0 : 2, 2: 1}
# #los valores 1, 2, 3, 5 serán índices del segundo array.
# b[1] = 2 % 2 = 0
# b[2] = 3 % 2 = 1 <- return índice
# b[3] = 0
# b[4] = 2
# b[5] = 2
#ele ementos dA son positivos (utilizar como índices)



