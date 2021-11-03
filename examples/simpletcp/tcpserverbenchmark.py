import socket

from sb.simplebenchmarking.simplebenchmark import SimpleBenchmark
from sb.simplebenchmarking.timing import func_timer


class TcpServerBenchmark(SimpleBenchmark):
    def __init__(self, host: str, port: int, connection_pool_size: int):
        self.server_address = (host, port)
        self.pool = [self.init() for _ in range(connection_pool_size)]
        self.transactions = []

    def init(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.connect(self.server_address)

        return s

    @func_timer
    def perform(self, transaction_count: int, message: str,  **kwargs):
        """The intent is to send small messages, less then 1024 bytes in len,
        read the reply back and record processing time."""
        for _ in range(transaction_count):
            for s in self.pool:
                sent, recv, error = 0, 0, False
                try:
                    sent = s.send(message.encode())
                    recv = s.recv(1024)
                except Exception as e:
                    print(e)
                    error = True
                finally:
                    if not recv:
                        error = True
                self.transactions.append((sent, recv, error))
        return len(self.transactions)

    def verify(self):
        return all(not item[2] for item in self.transactions)

    def finalize(self):
        for s in self.pool:
            try:
                s.send('Connection: Close'.encode())
            except socket.error as e:
                print(e)
            finally:
                s.close()