import abc
from dataclasses import dataclass


@dataclass
class ReportData:
    transaction_count: int
    total_time: float
    tps: float
    all_processed: bool

    def __str__(self):
        rep = f"Processed: {self.transaction_count} transactions " \
              f"in {self.total_time}\n" \
              f"TPS: {self.tps}\n" \
              f"All messages processed: {self.all_processed}\n"

        return rep


class SimpleBenchmark(object):
    def __init__(self):
        self._count = 0
        self._total_time = 0

    def run(self, *args, **kwargs):
        self._count, self._total_time = self.perform(*args, **kwargs)

    def init(self) -> None:
        """Initialization method"""
        pass

    @abc.abstractmethod
    def perform(self, *args, **kwargs) -> (int, float):
        """Run implemented logic and performance tests
        :param args:
        :param kwargs:
        :return: (int, float) -> (number of transactions, total time)"""

    @abc.abstractmethod
    def verify(self, *args) -> bool:
        """Verifies transactions run are correct
        :return: result of the run"""

    def finalize(self):
        """Clean any outstanding resources"""
        pass

    def get_transaction_count(self) -> int:
        """Provides transaction count
        :return: transaction count
        """
        return self._count

    def get_total_time(self):
        return self._total_time

    def get_tps(self, rounding: bool = True) -> float:
        """Provides transaction per second
        :return: TPS - Transaction Per Second
        """
        value = self._count / self._total_time
        return round(value, 1)

    def report(self, *args) -> ReportData:
        """Report on performance results
        :return: ReportData
        """

        report_data = ReportData(
            self.get_transaction_count(),
            self.get_total_time(),
            self.get_tps(),
            self.verify(*args)
        )

        return report_data
