from toolkit import two_time_convolution
import numpy as np

result = np.array([[ 0,1,4,6,4,1,0],
[ 1,6,17,24,17,6,1],
[ 4,17,40,54,40,17,4],
[ 6,24,54,72,54,24,6],
[ 4,17,40,54,40,17,4],
[ 1,6,17,24,17,6,1],
[ 0,1,4,6,4,1,0]])

filter_b = np.array([[1, 2, 1],
					 [2, 4, 2],
					 [1, 2, 1]])

size = len(result) - len(filter_b) + 1
filter_a = np.zeros((size, size), dtype=np.result_type(result))

for y in range(len(filter_a)):
	for x in range(len(filter_a[0])):
		filter_a[y][x] = result[y][x]
		result[y:y+len(filter_b), x:x+len(filter_b)] -= filter_a[y][x] * filter_b

print(filter_a)
print(np.result_type(result))
print(two_time_convolution(filter_a, filter_b))