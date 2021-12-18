""" 
pip install django-extensions
settings.py dopisać INSTALLED_APPS =[ ..., 'django-extensions', ...]
stworzyć folder srcripts a w nim scripts/__init__.py pusty

załadowanie danych:
python manage.py runscript cve_list_load # BEZ ROZSZRZERZENIA PY
"""

MAIN_URL = "https://nvd.nist.gov/vuln/data-feeds#JSON_FEED"

file_url = "https://nvd.nist.gov/feeds/json/cve/1.1/nvdcve-1.1-modified.json.zip"


def download():
    pass