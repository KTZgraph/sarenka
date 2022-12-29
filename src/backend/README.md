# posgresql
```sh
psql -U postgres
DROP DATABASE sarenka_users;
\q
```


```sh
psql -U postgres
CREATE DATABASE sarenka_users OWNER postgres;
\q
```

python manage.py makemigrations
python manage.py migrate users --database=users

```sh
psql -U postgres
CREATE DATABASE sarenka_vulnerabilities OWNER postgres;
\q
```

```sh
psql -U postgres
\l
\c  sarenka_users
\dt
SELECT * FROM users_useraccount;
```

```sh
python manage.py createsuperuser --database=users
```


# https://stackoverflow.com/questions/71389479/cant-connect-to-postgres-from-django-using-a-connection-service-file-on-window


