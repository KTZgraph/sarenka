from backend.settings.base import *

DEBUG = False
ALLOWED_HOSTS =[
    'sarenka-production.pl'
]


try:
    from backend.settings.local import *
except:
    print("Please create file 'prod.py' in folder backed/backend/settings")