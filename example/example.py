#  Copyright (c) ChernV (@otter18), 2021.

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

# TgFileLogger example
tg_files_logger = tg_logger.TgFileLogger(
    token=token,  # tg bot token
    users=users,  # list of user_id
    timeout=10  # default is 10 seconds
)

file_name = "test.txt"
with open(file_name, 'w') as example_file:
    example_file.write("Hello from tg_logger by otter18")

tg_files_logger.send(file_name, "Test file")

# And one more time...
logger.info("Finishing tg_logger demo")
