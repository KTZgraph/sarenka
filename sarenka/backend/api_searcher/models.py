"""
Modul przechowujący dane uwierzytelniające użytkownika do serwisów trzecich, które wymagają kont.
"""
from django.db import models


class CensysCredentialsModel(models.Model):
    """Model przechowujący informacje o danych uwierzytelniajacych użytkownika do serwisu http://censys.io/
    Może istnieć tylko jedna instancja przechowująca dane użytkownika"""
    api_id = models.CharField(max_length=72, unique=True, default="")
    secret = models.CharField(max_length=64, unique=True, default="")
    base_url = models.CharField(max_length=36, unique =True, default="https://censys.io/")
    api_url = models.CharField(max_length=48, unique=True, default="https://censys.io/api/v1")

    @classmethod
    def object(cls):
        return cls._default_manager.all().first() # Since only one item

    def save(self, *args, **kwargs):
        self.id = 1
        return super().save(*args, **kwargs)


class ShodanCredentialsModel(models.Model):
    """Model przechowujący informacje o danych uwierzytelniajacych użytkownika do serwisu https://www.shodan.io/
    Może istnieć tylko jedna instancja przechowująca dane użytkownika"""
    user = models.CharField(max_length=200, unique=True, default="")
    api_key = models.CharField(max_length=64, unique=True, default="")
    base_url = models.CharField(max_length=44, unique=True, default="https://www.shodan.io/")

    @classmethod
    def object(cls):
        return cls._default_manager.all().first() # Since only one item

    def save(self, *args, **kwargs):
        self.id = 1
        return super().save(*args, **kwargs)