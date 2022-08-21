#  Copyright (c) ChernV (@otter18), 2021.

import logging
from time import time, sleep
from typing import List

import telebot

# logging setup
logger = logging.getLogger(__name__)


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
                        self.bot.send_document(user_id, document=data, caption=caption, parse_mode="HTML")
                        logger.info("File %s successfully send to %s", file_path, user_id)
                        break
                    except Exception:
                        logger.exception("Exception while sending %s to %s:", file_path, user_id)
                        sleep(1)
