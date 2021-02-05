#  Copyright (c) ChernV (@otter18), 2021.

import logging
from logging import StreamHandler
from time import time, sleep
from typing import List

import telebot

# logging setup
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def setup(base_logger: logging.Logger,
          token: str = '',
          users: List[int] = [],
          timeout: int = 10,
          tg_format: str = '<b>%(name)s:%(levelname)s</b> - <code>%(message)s</code>'):
    """
    Setup TgLoggerHandler tool

    :param base_logger: base logging.Logger obj
    :param token: tg bot token to log form
    :param users: list of used_id to log to
    :param timeout: seconds for retrying to send log if error occupied
    :param tg_format: logging format for tg messages (html parse mode)

    :return: None
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
    # return base_logger


class TgLoggerHandler(StreamHandler):
    """Logger handler for tg_logger"""

    def __init__(self, token: str, users: List[int], timeout: int = 10):
        """
        Setup TgLoggerHandler class

        :param token: tg bot token to log form
        :param users: list of used_id to log to
        :param timeout: seconds for retrying to send log if error occupied
        """

        super().__init__()
        self.token = token
        self.users = users
        self.timeout = timeout

        self.bot = telebot.TeleBot(token=self.token)

    def emit(self, record):
        msg = self.format(record)
        for user_id in self.users:
            t0 = time()
            while time() - t0 < self.timeout:
                try:
                    self.bot.send_message(user_id, msg, parse_mode="HTML")
                    break
                except Exception as ex:
                    logger.exception("Exception while sending %s to %s:", msg, user_id)
                    sleep(1)


class TgFileLogger:
    """tg_logger tool to send files"""

    def __init__(self, token: str, users: List[int], timeout: int = 10):
        """
        Setup TgFileLogger tool

        :param token: tg bot token to log form
        :param users: list of used_id to log to
        :param timeout: seconds for retrying to send log if error occupied
        """

        self.token = token
        self.users = users
        self.timeout = timeout

        self.bot = telebot.TeleBot(token=self.token)

    def send(self, file_path: str, caption: str = ''):
        """
        Function to send file

        :param file_path: file path to log
        :param caption: text to file with file

        :return: None
        """

        with open(file_path, 'rb') as data:
            for user_id in self.users:
                t0 = time()
                while time() - t0 < self.timeout:
                    try:
                        self.bot.send_document(user_id, data=data, caption=caption, parse_mode="HTML")
                        logger.info("File %s successfully send to %s", file_path, user_id)
                        break
                    except Exception as ex:
                        logger.exception("Exception while sending %s to %s:", file_path, user_id)
                        sleep(1)
