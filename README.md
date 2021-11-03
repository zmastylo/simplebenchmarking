<h1 align="center">Welcome to simple benchmarking 👋</h1>
<p>
  <a href="https://www.npmjs.com/package/benchmarking" target="_blank">
    <img alt="Version" src="https://img.shields.io/npm/v/benchmarking.svg">
  </a>
  <a href="LICENSE" target="_blank">
    <img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-yellow.svg" />
  </a>
  <a href="https://twitter.com/zmastylo" target="_blank">
    <img alt="Twitter: zmastylo" src="https://img.shields.io/twitter/follow/zmastylo.svg?style=social" />
  </a>
</p>

> Simple benchmarking utilities.

## Install
Will be added later. From simplebenchmarking folder you will run:

```sh
pip3 install .
```

## Usage

```sh
examples/ folder has sample benchmarks with run.py
```

## Run tests

```sh
pytest tests
```

## Create your own benchmark
Subclass SimpleBenchmark class and provide implementation 
for abstract methods listed below. 

Ensure to wrap perform()
with @func_timer as depicted below. 
```
@func_timer
def perform(self, *args, **kwargs) -> (int, float):
    """Run implemented logic and performance tests
    :param args:
    :param kwargs:
    :return: (int, float) -> (number of transactions, total time)"""

def verify(self, *args) -> bool:

```

## How to improve the project

> Few extra things can be added to base Benchmark class:
```
-- CPU utilization
-- Memory usage
-- I/O stats
-- And other system related resources
```

## Author

👤 **Zbigniew Mastylo**

* Twitter: [@zmastylo](https://twitter.com/zmastylo)
* Github: [@zmastylo](https://github.com/zmastylo)
* LinkedIn: [@zmastylo](https://linkedin.com/in/zmastylo)

## Show your support

Give a ⭐️ if this project helped you!

## 📝 License

Copyright © 2021 [Zbigniew Mastylo](https://github.com/zmastylo).<br />
This project is [MIT](LICENSE) licensed.

***
_This README was generated with ❤️ by [readme-md-generator](https://github.com/kefranabg/readme-md-generator)_
