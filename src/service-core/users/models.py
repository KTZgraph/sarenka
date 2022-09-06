from django.db import models

# https://docs.djangoproject.com/en/4.1/topics/auth/customizing/#custom-users-admin-full-example
# PermissionsMixin potrzebne gdy robimy superusera czy kogos z dodatkowymi prawami jak .is_staff=True
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin,
)


class UserAccountManager(BaseUserManager):
    """Custom User Manager - pamiętać o dziedziczeniu"""

    def create_user(self, first_name, last_name, email, password=None):
        if not email:
            raise ValueError("Users must have an email address")

        email = self.normalize_email(email)  # JOHNDOE@GMAIL.COM -> JOHNDOE@gmail.com
        email = email.lower()

        user = self.model(first_name=first_name, last_name=last_name, email=email)

        # hashuje hasło
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, email, password=None):
        user = self.create_user(
            # wukorzstuje metodę z góry tej klasy
            first_name,
            last_name,
            email,
            password,
        )
        # flaga na user.is_admin = True - można logowac się jako admin Django
        # user.is_admin = True

        # flaga na user.is_staff = True - można logowac się jako admin Django
        user.is_staff = True

        # flaga na user.is_superuser = True - można zmieniać dane
        user.is_superuser = True

        user.save(using=self._db)
        return user


class UserAccount(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True, max_length=255)

    # defaultowo aktywny user
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # nasz customowy manager
    # porzbene do takich operacji na ORM takich jak User.objects.filter(email="joedoe@gmail.com")
    # porzbene do takich operacji na ORM takich jak User.objects.create_user() <-to nasze nadpisane żeby pola były takie jak chcę
    objects = UserAccountManager()

    # USERNAME_FIELD - pole przy pomocy które się loguję
    USERNAME_FIELD = "email"
    # REQUIRED_FIELDS - pola wymagane do tworzenia konta
    REQUIRED_FIELDS = ["first_name", "last_name"]

    def __str__(self):
        return self.email
