import argparse

from simplehttp.httpserverbenchmark import HttpServerBenchmark

parser = argparse.ArgumentParser(
    description='Run simplehttp server performance.'
)

parser.add_argument(
    "--url",
    type=str,
    default='http://localhost:9999',
    help='server host'
)

parser.add_argument(
    "--end_point", '-e',
    type=str,
    default='test',
    help='simplehttp server endpoint'
)

parser.add_argument(
    "--count", '-c',
    type=int,
    default=1000,
    help='number of transactions sent to destination server'
)

parser.add_argument(
    "--pool_size", '-ps',
    type=int,
    default=1,
    help='size of connection pool to destination server'
)


def main():
    benchmark = None
    try:
        args = vars(parser.parse_args())

        url = args['url']
        end_point = args['end_point']
        count = args['count']
        pool_size = args['pool_size']

        benchmark = HttpServerBenchmark(url, pool_size)
        benchmark.run(count, end_point=end_point)
        report_data = benchmark.report()
        print(report_data)
    except Exception as e:
        print(e)
    finally:
        benchmark.finalize()


if __name__ == "__main__":
    main()
