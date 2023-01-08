import numpy as np
import cv2
def two_time_convolution(filter_a, filter_b):
	size = len(filter_a) + len(filter_b) - 1
	result = np.zeros((size, size))
	for y_b in range(len(filter_b)):
		for x_b in range(len(filter_b[0])):
			tmp = filter_a * filter_b[y_b][x_b]
			result[y_b:y_b+len(filter_a), x_b:x_b+len(filter_a)] += tmp
	return result

def recover_filter_from_result(result, filter_b):
	size = len(result) - len(filter_b) + 1
	filter_a = np.zeros((size, size), dtype=np.result_type(result))
	for y in range(len(filter_a)):
		for x in range(len(filter_a[0])):
			filter_a[y][x] = result[y][x]
			result[y:y+len(filter_b), x:x+len(filter_b)] -= filter_a[y][x] * filter_b
	return filter_a