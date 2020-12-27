from pathlib import Path

from backend.settings.base import *

# class LogFileError(Exception):

# gdy plik logów nie istnieje
if not Path("logs").is_dir():
    dirname= Path('logs')
    dirname.mkdir()


if not Path('info_dev1.log').is_file():
    filename = Path('logs/info_dev1.log')
    filename.touch(exist_ok=True)  # will create file, if it exists will do nothing

if not Path('debug_dev1.log').is_file():
    filename = Path('logs/debug_dev1.log')
    filename.touch(exist_ok=True)  # will create file, if it exists will do nothing




LOGGING = {
    "version": 1,
    "loggers":{
        "django":{
            "handlers": ["file", "file2"],
            "level": "DEBUG",
        }
    },
    "handlers":{
        "file": {
            "level": "INFO",
            "class": "logging.FileHandler",
            "filename": "./logs/info_dev.log",
            "formatter": "simple_formatter",
        },
        "file2": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "filename": "./logs/debug_dev.log",
            "formatter": "simple_formatter2",
        }
    },
    "formatters":{
        "simple_formatter":{
            "format": "{levelname} {asctime} {module} {message}",
            "style": "{"
        },
        "simple_formatter2": {
            "format": "{levelname} {asctime} {module} {process:d} {thread:d} {message}",
            "style": "{"
        }
    }
}

