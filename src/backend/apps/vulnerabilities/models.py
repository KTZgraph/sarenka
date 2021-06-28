from django.db import models


class CWE(models.Model):
    code = models.CharField(max_length=10, unique=True)
    # krókie opisy z https://nvd.nist.gov/vuln/categories
    short_description = models.CharField(max_length=500)
    description = models.TextField()

    def __str__(self):
        return self.code


class CVE(models.Model):
    cwe = models.ForeignKey(CWE, on_delete=models.PROTECT, related_name='cve_list')
    code = models.CharField(max_length=15, unique=True)
    description = models.TextField()
    published = models.DateField()
    updated = models.DateField()

    def __str__(self):
        return self.code


class Vector(models.Model):
    VERSION = [
        ('3', 'CVSSV3'),
        ('2', 'CVSSV2'),
    ]
    SEVERITY = [
        ('0', 'LOW'),
        ('1', 'MEDIUM'),
        ('2', 'HIGH'),
    ]
    version = models.CharField(choices=VERSION, max_length=6)
    code = models.CharField(max_length=50)
    base_score = models.CharField(max_length=5)
    base_severity = models.CharField(choices=SEVERITY, max_length=6)
    exploitability_score = models.CharField(max_length=5)
    impact_score = models.CharField(max_length=5)
    cve = models.ForeignKey(CVE, on_delete=models.CASCADE, related_name='vector_list')

    def __str__(self):
        return self.code


class Reference(models.Model):
    is_confirmed = models.BooleanField()
    is_exploit = models.BooleanField()
    is_vendor_advisory = models.BooleanField()
    cve = models.ForeignKey(CVE, on_delete=models.CASCADE, related_name='reference_list')
    url = models.URLField()

    def __str__(self):
        return str(self.url)


class CPE(models.Model):
    VERSION = [
        ('2.2', 'CPE2.2'),
        ('2.3', 'CPE2.3')
    ]
    is_vulnerable = models.BooleanField()
    version = models.CharField(choices=VERSION, max_length=6)
    cve = models.ForeignKey(CVE, on_delete=models.CASCADE, related_name='cpe_list')
    code = models.CharField(max_length=500)

    def __str__(self):
        return self.code
