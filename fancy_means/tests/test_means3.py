import numpy as np
from time import time
from fancy_means import slow_means


def test_means():
    """
    """
    r = np.random.rand(10**5)
    tstart = time()
    [slow_means.mean3filter(r) for i in range(10)]
    tstop = time()
    time_slow = tstop - tstart
    try:
        from fancy_means import fast_means
        tstart = time()
        [fast_means.mean3filter3(r) for i in range(10)]
        tstop = time()
        time_fast = tstop - tstart
        assert time_slow > time_fast
    except ImportError:
        pass
