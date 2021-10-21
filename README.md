# log.py
A basic logging library for Python.

## Usage:
### - Instantiated:
Code:
```python
import logpy
from logpy.log import Levels

logger = logpy.Logger()
logger.log("Hello World!")
logger.log("Oh no, something went wrong!", Levels.error)
```

Terminal:
![img.png](images/img.png)

### - Non-instantiated:
Code:
```python
from logpy import Logger
from logpy.log import Levels

Logger.log("Hello World!")
Logger.log("Oh no, something went wrong!", Levels.error)
```

Terminal:
![img.png](images/img.png)

## Documentation:

## Requirements:
- Python 3.10
