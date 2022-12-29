from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)


class UserAccountManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError("Users must have an email address.")

        # normalizacja emaila
        email = self.normalize_email(email)  # do mały liter
        email = email.lower()

        user = self.model(email=email, name=name)

        user.set_password(password)
        # using=self._db zapisywanie do odpowiedniej bazy dancyh
        user.save(using=self._db)

        return user

    def create_analyst(self, email, name, password=None):
        user = self.create_user(email, name, password)
        user.is_analyst = True
        # using=self._db zapisywanie do odpowiedniej bazy dancyh
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password):
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)
        return user


class UserAccount(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    name = models.EmailField(max_length=255, unique=True)
    # https://www.shodan.io/
    SHODAN_API_KEY = models.CharField(max_length=32)
    # https://censys.io/
    CENSYS_API_ID = models.CharField(max_length=500)
    CENSYS_API_SECRET = models.CharField(max_length=500)
    # https://www.criminalip.io/developer/api/get-ip-summary
    CRIMINALIP_API_KEY = models.CharField(max_length=60)
    # https://github.com/knownsec/ZoomEye-python https://www.zoomeye.org/profile
    ZOOMEYE_API_KEY = models.CharField(max_length=36)
    # https://developers.notion.com/docs/create-a-notion-integration
    NOTION_TOKEN = models.CharField(max_length=50)
    # https://www.mongodb.com/docs/manual/reference/connection-string/
    MONGODB_CONNECTION_STRING = models.CharField(max_length=180)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    is_analyst = models.BooleanField(default=False)

    objects = UserAccountManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    def __str__(self) -> str:
        return self.email
