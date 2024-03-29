import numpy as np


def mean3filter(arr):
    arr_out = np.empty_like(arr)
    for i in range(1, arr.shape[0] - 1):
        arr_out[i] = np.sum(arr[i-1:i+2]) / 3
    arr_out[0] = (arr[0] + arr[1]) / 2
    arr_out[-1] = (arr[-1] + arr[-2]) / 2
    return arr_out
