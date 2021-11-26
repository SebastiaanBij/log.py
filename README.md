# <b><u>log.py</u></b>
[![Python Version Shield](https://img.shields.io/badge/Python%20Version-3.10-white?color=white&label=PyPi%20Downloads&logo=python&logoColor=white&style=for-the-badge)](https://www.python.org/downloads/release/python-3100/)
[![PyPi Downloads Shield](https://img.shields.io/pypi/dm/log.py?color=blue&label=PyPi%20Downloads&logo=pypi&logoColor=blue&style=for-the-badge)](https://pypi.org/project/log.py/)
[![License Shield](https://img.shields.io/github/license/sebastiaanbij/log.py?style=for-the-badge)](https://github.com/SebastiaanBij/log.py/blob/main/LICENSE)

## <b>📖 About:</b>
A basic logging library for Python with the capability to:
- save to files.
- have custom formats.
- have custom levels.
- be used instantiated.
- be used non-instantiated.

## <b>📝 Basic Usage:</b>
<i>(For more advanced uses, please refer to the given examples or the documentation.)</i>
### <u>Instantiated:</u>
- Code:
```python
from logpy import Logger
from logpy.log import Levels

logger = Logger()
logger.log("Hello World!")
logger.log("Oh no, something went wrong!", Levels.error)
```

- Terminal:\
![img.png](images/terminal_result.png)

### <u>Non-instantiated:</u>
- Code:
```python
from logpy import Logger
from logpy.log import Levels

Logger.slog("Hello World!")
Logger.slog("Oh no, something went wrong!", Levels.error)
```

- Terminal:\
![img.png](images/terminal_result.png)

## <b>🔧 Examples:</b>
[Click me!](https://github.com/SebastiaanBij/log.py/tree/main/examples)

## <b>📚 Documentation:</b>
[Click me!](https://sebastiaanbij.github.io/log.py/logpy.html)

## <b>❗ Requirements:</b>
- [Python 3.10](https://www.python.org/downloads/release/python-3100/)
