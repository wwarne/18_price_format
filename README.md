# Price Formatter

This script takes as input the price and displays it in a pretty format. It can be used as console-line application as well as programm interface.
Returns `None` if price can't be converted

## CLI USAGE
```
$ python3 format_price.py 1927.21
1 927.21
```

## Usage in your programs
```python
from format_price import format_price

pretty_price = format_price(your_old_bad_looking_price)

```

# Tests
To run unittests just type
```
$ python3 tests.py

...............
----------------------------------------------------------------------
Ran 15 tests in 0.002s

OK
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
