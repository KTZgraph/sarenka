from django.db import models

class CWE(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    #pole name z xmla to  krókie opisy jak  z https://nvd.nist.gov/vuln/categories 
    name = models.TextField(null=False)
    abstraction = models.CharField(max_length=100)
    structure = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    
    description = models.TextField(null=False)  
    extended_description = models.TextField(null=True)

    def __str__(self):
        return self.id