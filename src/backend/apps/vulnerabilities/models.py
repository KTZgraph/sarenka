from django.db import models
from django.db import IntegrityError, transaction
from base64 import b64encode


def encode_to_base64(value: str) -> str:
    """
    :param value:
    :return: base64 encoded string
    """
    str_bytes = value.encode('utf-8')
    base64_bytes = b64encode(str_bytes)
    base64_str = base64_bytes.decode('utf-8')
    return base64_str


class CWE(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=1500)
    abstraction = models.CharField(max_length=100)
    structure = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    description = models.CharField(max_length=1500)  # krókie opisy z https://nvd.nist.gov/vuln/categories
    extended_description = models.TextField(null=True)

    def __str__(self):
        return self.id


class Vector(models.Model):
    VERSION = [
        ('3.1', 'CVSSV3.1'),
        ('3.0', 'CVSSV3.0'),
        ('2.0', 'CVSSV2.0'),
    ]
    SEVERITY = [
        ('0', 'LOW'),
        ('1', 'MEDIUM'),
        ('2', 'HIGH'),
    ]
    id = models.CharField(primary_key=True, max_length=50, default='-1')  # base64 vector code
    version = models.CharField(choices=VERSION, max_length=6)
    code = models.CharField(max_length=50, unique=True)
    base_score = models.CharField(max_length=5)
    base_severity = models.CharField(choices=SEVERITY, max_length=6)
    exploitability_score = models.CharField(max_length=5)
    impact_score = models.CharField(max_length=5)

    def save(self, *args, **kwargs):
        self.id = encode_to_base64(self.code)
        super(Vector, self).save(*args, **kwargs)

    def __str__(self):
        return self.code


class CVE(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    cwe = models.ForeignKey(CWE, on_delete=models.PROTECT, related_name="cwe_list")
    description = models.TextField()
    published = models.DateField()
    updated = models.DateField()
    vectors = models.ManyToManyField(Vector)

    def __str__(self):
        return self.id


class Reference(models.Model):
    is_confirmed = models.BooleanField()
    is_exploit = models.BooleanField()
    is_vendor_advisory = models.BooleanField()
    cve = models.ForeignKey(CVE, on_delete=models.CASCADE)
    url = models.URLField()

    def __str__(self):
        return str(self.url)


class CPE(models.Model):
    VERSION = [
        ('2.2', 'CPE2.2'),
        ('2.3', 'CPE2.3')
    ]
    id = models.CharField(primary_key=True, max_length=200, default='-1')  # base64 CPE code
    is_vulnerable = models.BooleanField()
    version = models.CharField(choices=VERSION, max_length=6)
    cve = models.ForeignKey(CVE, on_delete=models.CASCADE)
    code = models.CharField(max_length=500)

    def save(self, *args, **kwargs):
        self.id = encode_to_base64(self.code)
        super(CPE, self).save(*args, **kwargs)

    def __str__(self):
        return self.code
