# ![tg_logo](https://raw.githubusercontent.com/otter18/tg_logger/master/img/telegram-icon.png) Telegram logger [![GitHub Repo stars](https://img.shields.io/github/stars/otter18/tg_logger?style=social)](https://github.com/otter18/tg_logger/stargazers)
[![](https://img.shields.io/pypi/v/tg-logger.svg)](https://pypi.org/project/tg-logger/)
[![](https://img.shields.io/pypi/pyversions/tg-logger.svg)](https://pypi.org/project/tg-logger/)
[![GitHub](https://img.shields.io/github/license/otter18/tg_logger)](https://github.com/otter18/tg_logger/blob/main/LICENSE)



Bridging python logging and files to tg bot

## Installation & Usage
- Available by `pip install tg-logger`
- Use with `import tg_logger`

## Examples
### TgLogger example
```python
import logging
import tg_logger

# Telegram data
token = "1234567890:AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
users = [1111111111]

# Base logger
logger = logging.getLogger('foo')
logger.setLevel(logging.INFO)

# Logging bridge setup
tg_logger.setup(logger, token=token, users=users)

# Test
logger.info("Hello from tg_logger by otter18")
```

### TgFileLogger example
```python
import logging
import tg_logger

# Telegram data
token = "1234567890:AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
users = [1111111111]

# TgFileLogger example
tg_files_logger = tg_logger.TgFileLogger(
    token=token,  # tg bot token
    users=users,  # list of user_id
    timeout=10  # 10 seconds by default
)

file_name = "test.txt"
with open(file_name, 'w') as example_file:
    example_file.write("Hello from tg_logger by otter18")

tg_files_logger.send(file_name, "Test file")
```

### Example screenshot
![example_scr](https://raw.githubusercontent.com/otter18/tg_logger/master/img/example_scr.png)

## QA
### How to create a telegram bot? How to get `token` and `user_id`?
- To create bot use official [BotFather](https://t.me/BotFather) bot (descibed [here](https://core.telegram.org/bots#6-botfather))
- To get `user_id` use special bots (e.g. [@userinfobot](https://t.me/userinfobot), [@JsonDumpBot](https://t.me/JsonDumpBot))
