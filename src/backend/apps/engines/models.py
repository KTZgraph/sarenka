from django.db import models


class CensysCredentials(models.Model):
    class CensysObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(pk=1)

    api_id = models.CharField(max_length=72, unique=True, default="")
    secret = models.CharField(max_length=64, unique=True, default="")
    base_url = models.CharField(max_length=36, unique=True, default="https://censys.io/")
    api_url = models.CharField(max_length=48, unique=True, default="https://censys.io/api/v1")
    credentials = CensysObjects()  # custom manager

    @classmethod
    def object(cls):
        return cls._default_manager.all().first()  # Since only one item

    def save(self, *args, **kwargs):
        self.id = 1
        return super().save(*args, **kwargs)


class ShodanCredentials(models.Model):
    class ShodanObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(pk=1)

    user = models.CharField(max_length=200, unique=True, default="")
    api_key = models.CharField(max_length=64, unique=True, default="")
    base_url = models.CharField(max_length=44, unique=True, default="https://www.shodan.io/")
    api_url = models.CharField(max_length=62, unique=True, default="https://developer.shodan.io/api")
    credentials = ShodanObjects()  # custom manager

    @classmethod
    def object(cls):
        return cls._default_manager.all().first()  # Since only one item

    def save(self, *args, **kwargs):
        self.id = 1
        return super().save(*args, **kwargs)
