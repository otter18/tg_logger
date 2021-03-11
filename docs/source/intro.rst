Introduction
============

Tg-logger is took for bridging python logging and files to tg bot

Installation & Usage
********************
.. code:: bash

    pip install tg-logger
.. code:: python

    import tg_logger


Screenshot
**********

.. image:: https://raw.githubusercontent.com/otter18/tg_logger/master/img/example_scr.png
  :alt: example screenshot


Examples
********

Simple logging
##############
.. code:: python

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


Flask logging
#############
.. code:: python

    from flask import Flask
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


TgFileLogger example
####################

.. code:: python

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



