import cython
cimport numpy as np
import numpy as np

@cython.boundscheck(False)
def mean3filter3(double[::1] arr):
    cdef double[::1] arr_out = np.empty_like(arr)
    cdef int i
    for i in range(1, arr.shape[0]-1):
        arr_out[i] = (arr[i-1] + arr[i] + arr[i+1] + arr[i+2]) / 3
    arr_out[0] = (arr[0] + arr[1]) / 2
    arr_out[-1] = (arr[arr.shape[0]-1] + arr[arr.shape[0]-2]) / 2
    return np.asarray(arr_out)
