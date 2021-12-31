#  Copyright (c) ChernV (@otter18), 2021.

from .files import *
from .handler import *

import logging
from typing import List


def setup(base_logger: logging.Logger = logging.getLogger(),
          token: str = '',
          users: List[int] = [],
          timeout: int = 10,
          tg_format: str = '<b>%(name)s:%(levelname)s</b> - <code>%(message)s</code>'):
    """
    Setup TgLogger

    :param base_logger: base logging.Logger obj
    :param token: tg bot token to log form
    :param users: list of used_id to log to
    :param timeout: seconds for retrying to send log if error occupied
    :param tg_format: logging format for tg messages (html parse mode)

    :return: logging.StreamHandler
    """
    # Logging format
    formatter = logging.Formatter(tg_format)

    # Setup TgLoggerHandler
    tg_handler = TgLoggerHandler(
        token=token,  # tg bot token
        users=users,  # list of user_id
        timeout=timeout  # default value is 10 seconds
    )
    tg_handler.setFormatter(formatter)
    base_logger.addHandler(tg_handler)

    return tg_handler
