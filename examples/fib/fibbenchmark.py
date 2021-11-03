from typing import Callable

from sb.simplebenchmarking.simplebenchmark import SimpleBenchmark
from sb.simplebenchmarking.timing import func_timer


def recursive_fib(m):
    if m == 0 or m == 1:
        return m
    return recursive_fib(m-1) + recursive_fib(m-2)


def iterative_fib(m):
    if m == 0 or m == 1:
        return m

    a, b = 0, 1
    f = 0
    for _ in range(1, m):
        f = a + b
        a = b
        b = f

    return f


class FibBenchmark(SimpleBenchmark):
    def __init__(self, func: Callable):
        self.func = func
        self.transactions = []

    def init(self) -> None:
        pass

    @func_timer
    def perform(self, n: int, transaction_count: int, **kwargs) -> (int, float):
        for _ in range(transaction_count):
            self.transactions.append(self.func(n))

        return len(self.transactions)

    def verify(self, *args) -> bool:
        return True

    def finalize(self):
        self.transactions.clear()

