import os
from typing import Callable

import psutil

from fib.fibbenchmark import FibBenchmark, recursive_fib, iterative_fib


def main(fib_func: Callable):
    benchmark = FibBenchmark(func=fib_func)
    try:
        benchmark.run(n=35, transaction_count=1)
        report_data = benchmark.report()
        print(report_data)
    except Exception as e:
        print(e)
    finally:
        benchmark.finalize()


if __name__ == "__main__":
    pid = os.getpid()
    p = psutil.Process(pid)
    result = p.cpu_times()
    print(result)
    res_perc = p.cpu_percent(interval=1.0)
    print(res_perc)
    for func in [recursive_fib, iterative_fib]:
        main(func)

