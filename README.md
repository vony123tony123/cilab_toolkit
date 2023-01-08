# cilab_toolkit

## two_time_convolution 使用方式 
two_time_convolution(filter_a, filter_b) \
先做filter_a遮罩再做filter_b遮罩等於一次什麼遮罩\
filter_b可視作提供權重

## recover_filter_from_result 使用方式 
recover_filter_from_result(result, filter_b) \
給結果遮罩和filter_b遮罩，回傳filter_a遮罩
