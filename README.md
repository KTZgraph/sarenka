# BUG z Django 4.1.2. działała pusta baza default:{}

sarenka\src\backend\backend\settings.py

```python
# na kiedyś https://stackoverflow.com/questions/71389479/cant-connect-to-postgres-from-django-using-a-connection-service-file-on-window
DATABASES = {
    # chce na siłę migracje orbić do tej bazy, a nie może być pusta
    # BUG - to też nei pomaga python manage.py migrate auth --database=users
    # BUG z Django 4.1.2. działała pusta baza default:{}
    "default": {
        # BUG musi być engine od tej wersji
        # "ENGINE": "django.db.backends.sqlite3",
        # "NAME": BASE_DIR / "db.sqlite3",
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "sarenka_users",
        "USER": "postgres",
        "PASSWORD": "password",
    },
    "users": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "sarenka_users",
        "USER": "postgres",
        "PASSWORD": "password",
        # "OPTIONS": {
        #     "service": "sarenka_users_db",
        #     "passfile": ".sarenka_vulnerabilities_pgpass",
        # },
    },
    "vulnerabilities": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "sarenka_vulnerabilities",
        "USER": "postgres",
        "PASSWORD": "password",
        # "OPTIONS": {
        #     "service": "sarenka_vulnerabilities_db",
        #     "passfile": ".sarenka_vulnerabilities_pgpass",
        # },
    },
}
```
