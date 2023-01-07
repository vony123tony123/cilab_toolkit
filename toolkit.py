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
