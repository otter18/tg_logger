from setuptools import setup, find_packages

setup(
    name="tg_logger",
    version="3.2",
    description="A tool to bridge python logging and user files to telegram bot",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="ChernV (otter18)",
    author_email="vchern185@gmail.com",
    url="https://github.com/otter18/tg_logger",
    packages=find_packages(),
    install_requires=[
        "pyTelegramBotAPI==3.7.6",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
