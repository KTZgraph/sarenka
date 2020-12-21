from backend.settings.base import *

try:
    from backend.settings.local import *
except:
    print("Please create file 'test.py' in folder backed/backend/settings")