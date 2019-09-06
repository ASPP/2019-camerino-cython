import cython
import numpy as np
cimport numpy as np

DTYPE = np.double
ctypedef np.double_t DTYPE_t

@cython.boundscheck(False)
@cython.wraparound(False)
def mean3filter3(np.ndarray[DTYPE_t, ndim=1] arr):
    cdef np.ndarray[DTYPE_t, ndim=1] arr_out = np.empty_like(arr)
    cdef int i
    for i in range(1, arr.shape[0]-1):
        arr_out[i] = (arr[i-1] + arr[i] + arr[i+1]) / 3
    arr_out[0] = (arr[0] + arr[1]) / 2
    arr_out[arr.shape[0]-1] = (arr[arr.shape[0]-1] + arr[arr.shape[0]-2]) / 2
    return np.asarray(arr_out)