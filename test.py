from toolkit import two_time_convolution
import numpy as np

filter_a = np.array([[3,-2,3],[-2,-4,-2],[3,-2,3]])

filter_b = np.array([[1, 1, 1],
					 [1, 1, 1],
					 [1, 1, 1]])

# size = len(result) - len(filter_b) + 1
# filter_a = np.zeros((size, size), dtype=np.result_type(result))

# for y in range(len(filter_a)):
# 	for x in range(len(filter_a[0])):
# 		filter_a[y][x] = result[y][x]
# 		result[y:y+len(filter_b), x:x+len(filter_b)] -= filter_a[y][x] * filter_b

# print(filter_a)
# print(np.result_type(result))
print(two_time_convolution(filter_b, filter_a))