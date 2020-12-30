from pathlib import Path

from backend.settings.base import *


# gdy plik logów nie istnieje
if not Path("logs").is_dir():
    dir_name= Path('logs')
    dir_name.mkdir()

if not Path('info_dev.log').is_file():
    file_name = Path('logs/info_dev.log')
    file_name.touch(exist_ok=True)  # will create file, if it exists will do nothing

if not Path('debug_dev.log').is_file():
    file_name = Path('logs/debug_dev.log')
    file_name.touch(exist_ok=True)  # will create file, if it exists will do nothing




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

