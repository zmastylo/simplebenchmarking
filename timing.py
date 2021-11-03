import time
from functools import wraps


def func_timer(function):
    @wraps(function)
    def timer(*args, **kwargs):
        beg = time.perf_counter()
        result = function(*args, **kwargs)
        end = time.perf_counter()

        total_time = end-beg
        return result, total_time
    return timer
