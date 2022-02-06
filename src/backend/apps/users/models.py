from django.db import models
from django.contrib.auth.models import User

class AppUser(User):
    censys_api_id = models.CharField(max_length=72, unique=True, default="")
    censys_secret = models.CharField(max_length=64, unique=True, default="")
    shodan_username = models.CharField(max_length=200, unique=True, default="")
    shodan_api_key = models.CharField(max_length=64, unique=True, default="")
