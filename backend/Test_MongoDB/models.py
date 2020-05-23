from django.db import models
class Test_mongo(models.Model):
    text = models.CharField(max_length=200)    
    def __str__(self):
        return self.text