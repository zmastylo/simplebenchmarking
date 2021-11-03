import requests
from requests.adapters import HTTPAdapter

from sb.simplebenchmarking.simplebenchmark import SimpleBenchmark
from sb.simplebenchmarking.timing import func_timer


class HttpServerBenchmark(SimpleBenchmark):
    def __init__(self, url: str, connection_pool_size: int):
        self.url = url
        self.max_size = connection_pool_size
        self.session = requests.Session()
        self.transactions = []
        self.init()

    def init(self):
        req_adapter = HTTPAdapter(
            pool_connections=self.max_size, pool_maxsize=self.max_size
        )
        self.session.mount(self.url, adapter=req_adapter)

    @func_timer
    def perform(self, num_requests: int, message={"account": "example"}, **kwargs):
        end_point = kwargs['end_point']
        end_point = self.url + '/' + end_point
        for _ in range(num_requests):
            error = False
            try:
                reply = self.session.post(end_point, json=message)
            except Exception as e:
                print(e)
                error = True
            self.transactions.append((reply, error))
        return len(self.transactions)

    def verify(self, message={"account": "example"}):
        def check_item(item):
            status_code = item[0].status_code
            data = item[0].json()
            error = item[1]

            return status_code == 200 and data == message and not error

        return all(check_item(item) for item in self.transactions)

    def finalize(self):
        self.session.close()
