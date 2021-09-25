def solution(A):
	"""An program that finds the missing element from an array"""
	# Specs:
	# 1.- N is an integer within the range [0...100,000]
	# 2.- The elements of A are all distinct
	# 3.- Each element of A is an integer within the range [1...(N+1)]
	# Algoritmo:
	# Sumar todos los elementos
	# Obtener la suma de Gauss de los elementos:
	# S = n[2a+(n-1)d]2
	if not A:
		return 1

	sum_of_A = sum(A)
	gauss_sum = ((len(A) + 1)*(2 * min(A) + (len(A)))) / 2
	result = int(gauss_sum) - sum_of_A
	if result == 0:
		return max(A)+1
	elif (min(A)) != 1 and max(A) > len(A):
		return (min (A) - 1)
	else:
		return result



if __name__ == '__main__':
	print(solution([5]))

