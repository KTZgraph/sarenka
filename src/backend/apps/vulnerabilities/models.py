import black
from django.db import models

class CWE(models.Model):
    code = models.CharField(max_length=20, unique=True)
    #pole name z xmla to  krókie opisy jak  z https://nvd.nist.gov/vuln/categories 
    name = models.TextField(null=False)
    abstraction = models.CharField(max_length=100)
    structure = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    description = models.TextField(null=False)  
    extended_description = models.TextField(null=True)

    def __str__(self) -> str:
        return self.code


#-------------------- CVE -------------------------
class Version(models.Model):
    """cve.data_version"""
    version = models.DecimalField(max_digits=5, decimal_places=2, null=False, blank=False, unique=True) #wiele cve ma wersje
    def __str__(self) -> str:
        return str(self.version)

class Assigner(models.Model):
    """cve.data_version.ASSIGNER"""
    email = models.EmailField(max_length=30, blank=False, unique=True)
    def __str__(self) -> str:
        return self.email

class Format(models.Model):
    """cve.data_format"""
    format = models.CharField(max_length=20, null=False, blank=False, unique=True)
    def __str__(self) -> str:
        return self.format

class CVE(models.Model):
    "cve.CVE_data_meta.ID"
    code = models.CharField(max_length=20, unique=True, null=False, blank=False)
    # no cwe CVE-2002-2440
    cwe = models.ForeignKey(CWE, on_delete=models.CASCADE, null=True, default=None) 
    version = models.ForeignKey(Version, on_delete=models.CASCADE, null=True, default=None) # 1 wersja
    assigner = models.ForeignKey(Assigner, on_delete=models.CASCADE, null=True, default=None) # 1 wersja
    format = models.ForeignKey(Format, on_delete=models.CASCADE, null=True, default=None) # 1 wersja
    
    published = models.DateField(blank=False, null=False)
    modified = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return self.code


class Reference(models.Model):
    """cve.references.reference_data[listId].name
       cve.references.reference_data[listId].url
    """
    class Meta:
        unique_together = ('name', 'url')

    name = models.CharField(max_length=200, null=False, blank=False)
    url = models.URLField(max_length=500, null=False, blank=False) 
    cve = models.ManyToManyField(CVE)

    def __str__(self) -> str:
        return self.name

class Refsource(models.Model):
    """cve.references.reference_data[listId].refsource"""
    name = models.CharField(max_length=30, null=False, blank=False, unique=True)
    reference = models.ManyToManyField(Reference)

    def __str__(self) -> str:
        return self.name

class Tag(models.Model):
    """cve.references.reference_data[listId].tags[listId]"""
    name = models.CharField(max_length=20, null=False, blank=False, unique=True)
    reference = models.ManyToManyField(Reference)
    def __str__(self) -> str:
        return self.name


# ---    "configurations" :
class CPEMatch(models.Model):
    """cve.configurations.nodes[listId].cpe_match[listId]"""
    cve = models.ManyToManyField(CVE)
    is_vulnerable = models.BooleanField()
    uri = models.CharField(max_length=512, null=False, blank=False)


# ---- "impact"
class Vector(models.Model):
    vector = models.CharField(max_length=44, blank=False, null=False, unique=True)

    def __str__(self) -> str:
        return self.vector

# ----------------- impact.baseMetricV2 -----------------
class CVSSV2(models.Model):
    vector = models.ForeignKey(Vector, on_delete=models.CASCADE, null=False, blank=False)
    version = models.DecimalField(max_digits=5, decimal_places=2, null=False, blank=False)
    ACCESS_VECTOR = [
        ('NETWORK', 'network'),
        ('LOCAL', 'local'),
    ]
    access_vector = models.CharField(max_length=20, choices=ACCESS_VECTOR)
    ACCESS_COMPLEXITY = [
        ('LOW', 'low'),
        ('HIGH', 'high')
    ]
    access_complexity = models.CharField(max_length=20, choices=ACCESS_COMPLEXITY)
    AUTHENTICATION = [
        ('NONE', 'none'),
        ('SINGLE', 'single')
    ]
    authentication = models.CharField(max_length=20, choices=AUTHENTICATION)
    CONFIDENTIALITY_IMPACT = [
        ('HIGH', 'high'),
        ('PARTIAL', 'partial'),
        ('COMPLETE', 'complete'),
        ('NONE', 'none'),
    ]
    confidentiality_impact = models.CharField(max_length=20, choices=CONFIDENTIALITY_IMPACT)
    INTEGRITY_IMPACT = [
        ('NONE', 'none'),
        ('HIGH', 'high'),
        ('PARTIAL', 'partial'),
        ('COMPLETE', 'complete'),
    ]
    integrity_impact = models.CharField(max_length=20, choices=INTEGRITY_IMPACT)
    AVAIALABILITY_IMPACT = [
        ('COMPLETE', 'complete'),
        ('PARTIAL', 'partial'),
        ('NONE', 'none'),
    ]
    availability_impact = models.CharField(max_length=20, choices=AVAIALABILITY_IMPACT)
    base_score = models.DecimalField(max_digits=5, decimal_places=2, null=False, blank=False)


class BaseMetricV2(models.Model):
    cve = models.ManyToManyField(CVE, null=True, blank=True)
    cvss_v2 = models.ForeignKey(CVSSV2, on_delete=models.CASCADE, null=True, blank=True)
    SEVERITY = [
        ('HIGH', 'high'),
        ('MEDIUM', 'medium'),
        ('LOW', 'low'),
    ]
    severity = models.CharField(max_length=20, choices=SEVERITY)
    exploitability_score = models.DecimalField(max_digits=5, decimal_places=2, null=False, blank=False)
    impact_score = models.DecimalField(max_digits=5, decimal_places=2, null=False, blank=False)
    is_obtain_all_privilege  = models.BooleanField()
    is_obtain_user_privilege = models.BooleanField()
    is_obtain_other_privilege = models.BooleanField()
    # CVE-2016-0099 nie ma UserInteractionRequired
    is_user_interaction_required = models.BooleanField(default=None, blank=True, null=True)

# ----------------- impact.baseMetricV3 -----------------
class CVSSV3(models.Model):
    version = models.DecimalField(max_digits=5, decimal_places=2, null=False, blank=False)
    vector = models.ForeignKey(Vector, on_delete=models.CASCADE)
    ATTACK_VECTOR = [
        ('NETWORK', 'network'),
        ('LOCAL', 'local'),
    ]
    attack_vector = models.CharField(max_length=20, choices=ATTACK_VECTOR)
    ATTACK_COMPLEXITY = [
        ('LOW', 'low'),
        ('HIGH', 'high'),
    ]
    attack_complexity = models.CharField(max_length=20,choices=ATTACK_COMPLEXITY)
    PRIVILEGES_REQUIRED = [
        ('NONE', 'none'),
        ('LOW', 'low'),
    ]
    privileges_required = models.CharField(max_length=20, choices=PRIVILEGES_REQUIRED)
    USER_INTERACTION = [
        ('NONE', 'none')
    ]
    user_interaction = models.CharField(max_length=20, choices=USER_INTERACTION)
    SCOPE = [
        ('UNCHANGED', 'unchanged')
    ]
    scope = models.CharField(max_length=20, choices=SCOPE, null=True)
    CONFIDENTIALITY_IMPACT = [
        ('HIGH', 'high'),
        ('PARTIAL', 'partial'),
        ('COMPLETE', 'complete'),
        ('NONE', 'none'),
    ]
    confidentiality_impact = models.CharField(max_length=20, choices=CONFIDENTIALITY_IMPACT)
    INTEGRITY_IMPACT = [
        ('NONE', 'none'),
        ('HIGH', 'high'),
        ('PARTIAL', 'partial'),
        ('COMPLETE', 'complete'),
    ]
    integrity_impact = models.CharField(max_length=20, choices=INTEGRITY_IMPACT)
    AVAIALABILITY_IMPACT = [
        ('COMPLETE', 'complete'),
        ('PARTIAL', 'partial'),
        ('NONE', 'none'),
        ('HIGH', 'high'),
    ]
    availability_impact = models.CharField(max_length=20, choices=AVAIALABILITY_IMPACT)
    base_score = models.DecimalField(max_digits=5, decimal_places=2, null=False, blank=False)
    BASE_SEVERITY = [ # baseMetricV3
        ('CRITICAL', 'critical'),
        ('HIGH', 'high'),
        ('CRITICAL', 'critical'),
    ]
    base_severity = models.CharField(max_length=20, choices=BASE_SEVERITY)

class BaseMetricV3(models.Model):
    cve = models.ManyToManyField(CVE)
    cvss_v3 = models.ForeignKey(CVSSV3, on_delete=models.CASCADE)
    exploitability_score = models.DecimalField(max_digits=5, decimal_places=2, null=False, blank=False)
    impact_score = models.DecimalField(max_digits=5, decimal_places=2, null=False, blank=False)
