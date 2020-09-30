from backend.settings.base import *

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
            "filename": "./logs/info_dev1.log",
            "formatter": "simple_formatter",
        },
        "file2": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "filename": "./logs/debug_dev1.log",
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

try:
    from backend.settings.local import *
except:
    print("Please create file 'local.py' in folder backed/backend/settings")