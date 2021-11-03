import argparse

from simpletcp.tcpserverbenchmark import TcpServerBenchmark

parser = argparse.ArgumentParser(
    description='Simple tcp server benchmark.'
)

parser.add_argument(
    "--count", '-c',
    type=int,
    default=10,
    help='number of transactions sent to destination server'
)

parser.add_argument(
    "--pool_size", '-ps',
    type=int,
    default=1,
    help='size of connection pool to destination server'
)

parser.add_argument(
    "--host",
    type=str,
    default='localhost',
    help='server host'
)

parser.add_argument(
    "--port", '-p',
    type=int,
    default=9999,
    help='server port'
)


def main():
    args = vars(parser.parse_args())

    count = args['count']
    pool_size = args['pool_size']
    host = args['host']
    port = args['port']

    benchmark = TcpServerBenchmark(host, port, pool_size)
    try:
        benchmark.run(count)
        benchmark.report()
    except Exception as e:
        print(e)
    finally:
        benchmark.finalize()


if __name__ == "__main__":
    main()
