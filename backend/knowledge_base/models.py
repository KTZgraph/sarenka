from django.db import models

# Create your models here.
class Knowledge_base(models.Model):
    number_cwe = models.IntegerField(unique=True)
    definition = models.CharField(max_length=2000)