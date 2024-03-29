# ![tg_logo](https://raw.githubusercontent.com/otter18/tg_logger/master/img/telegram-icon.png) Telegram logger [![GitHub Repo stars](https://img.shields.io/github/stars/otter18/tg_logger?style=social)](https://github.com/otter18/tg_logger/stargazers)
[![Pypi version](https://img.shields.io/pypi/v/tg-logger.svg)](https://pypi.org/project/tg-logger/)
[![Downloads](https://static.pepy.tech/personalized-badge/tg-logger?period=total&units=international_system&left_color=grey&right_color=orange&left_text=Downloads)](https://pepy.tech/project/tg-logger)
[![GitHub](https://img.shields.io/github/license/otter18/tg_logger)](https://github.com/otter18/tg_logger/blob/main/LICENSE)
[![Documentation Status](https://readthedocs.org/projects/tg-logger/badge/?version=latest)](https://tg-logger.readthedocs.io/en/latest/?badge=latest)

<!-- [![Pyversions](https://img.shields.io/pypi/pyversions/tg-logger.svg)](https://pypi.org/project/tg-logger/) -->

Bridging python logging and files to tg bot

Documentation is available at [Read the Docs](https://tg-logger.readthedocs.io/)

Demo is available [@tg_logger_demo_bot](https://t.me/tg_logger_demo_bot), [[repo](https://github.com/otter18/tg-logger-demo-bot)]

![intro_img](https://raw.githubusercontent.com/otter18/tg_logger/main/img/intro.jpeg)

## 🗂 Table of Contents
- [Installation & Usage](#-installation--usage)
- [Screenshot](#-screenshot)
- [Examples](#-examples)
    * [Simple logging](#simple-logging)
    * [Flask logging](#flask-logging)
    * [Setting extra parameters to handler](#setting-extra-parameters-to-handler)
    * [TgFileLogger example](#tgfilelogger-example)
- [FQA](#-fqa)
    * [How to create a telegram bot?](#how-to-create-a-telegram-bot)
    * [How to get **token** and **user_id**?](#how-to-get-token-and-user_id)

## 🚀 Installation & Usage
- Available by `pip install tg-logger`
- Use with `import tg_logger`

## 📱 Screenshot
![example_scr](https://raw.githubusercontent.com/otter18/tg_logger/master/img/example_scr.png)

## 📖 Examples
### Simple logging
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

### Flask logging
```python
from flask import Flask
import logging
import tg_logger

# Telegram data
token = "1234567890:AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
users = [1111111111]

# Flask app setup
app = Flask(__name__)

app.logger.setLevel(logging.ERROR) # flask logger
tg_logger.setup(app.logger, token=token, users=users) # bridge setup


@app.route('/')
def hello_world():
    return 'Hello, World!'


if __name__ == '__main__':
    app.run()

```

### Setting extra parameters to handler

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
handler = tg_logger.setup(logger, token=token, users=users)

# Setting extra params
handler.setLevel(logging.DEBUG)

# Test
logger.info("Hello from tg_logger by otter18")
```

### TgFileLogger example
```python
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

## 🔎 FQA
### How to create a telegram bot? 
- To create bot use official [BotFather](https://t.me/BotFather) bot (descibed [here](https://core.telegram.org/bots#6-botfather))
### How to get **token** and **user_id**?
- Use [@tg_logger_demo_bot](https://t.me/tg_logger_demo_bot) with command `/id`
- Bot's **token** is shown after new bot is made
- To get **user_id** use special bots (e.g. [@userinfobot](https://t.me/userinfobot), [@JsonDumpBot](https://t.me/JsonDumpBot))

