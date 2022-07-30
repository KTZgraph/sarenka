# CWE (Common Weakness Enumeration)

```python
class CWE(models.Model):
    code = models.CharField(max_length=20, unique=True)
    name = models.TextField(null=False)
    abstraction = models.CharField(max_length=100)
    structure = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    description = models.TextField(null=False)
    extended_description = models.TextField(null=True)
```

- /api/vulns/cwes - lista wszsytkich CWE (< 900>)
- /api/vulns/cwes/${id} - jedno CWE ze wszsytkimi szczegółami
- /api/vulns/cwes/${id}/cves - wszystkie cve

---

---

# CVE (Common Vulnerabilities and Exposures)

## Version

```python
class Version(models.Model):
    version = models.DecimalField(max_digits=5, decimal_places=2, null=False, blank=False, unique=True)
```

- /api/vulns/versions - wszystkie wersje
- /api/vulns/versions/${id} - konkretna wersja
- /api/vulns/versions/${id}/cves - wszsytkie idki CVEs

---

## Assigner

```python
class Assigner(models.Model):
    email = models.EmailField(max_length=30, blank=False, unique=True)
```

- /api/vulns/assigners
- /api/vulns/assigners/${id}
- /api/vulns/assigners/${id}/cves

---

## Format

```python
class Format(models.Model):
    format = models.CharField(max_length=20, null=False, blank=False, unique=True)
```

- /api/vulns/fromats
- /api/vulns/fromats/${id}
- /api/vulns/fromats/${id}/cves

---

## CVE

```python
class CVE(models.Model):
    code = models.CharField(max_length=20, unique=True, null=False, blank=False)
    # no cwe CVE-2002-2440
    cwe = models.ForeignKey(CWE, on_delete=models.CASCADE, null=True, default=None)
    version = models.ForeignKey(Version, on_delete=models.CASCADE, null=True, default=None)
    assigner = models.ForeignKey(Assigner, on_delete=models.CASCADE, null=True, default=None)
    format = models.ForeignKey(Format, on_delete=models.CASCADE, null=True, default=None)

    published = models.DateField(blank=False, null=False)
    modified = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
```

- /api/vulns/cves - lista wszystkich cve od najnowszego - tabelka na froncie
- /api/vulns/cves/${id} - pojedyncze cve ze szczegółami
- /api/vulns/cves/${id}/cwes - same idki
- /api/vulns/cves/${id}/versions - same idki

---

---

# Reference, Refsource, Tag

## Reference

```python
class Reference(models.Model):
    class Meta:
        unique_together = ('name', 'url')

    name = models.CharField(max_length=200, null=False, blank=False)
    url = models.URLField(max_length=500, null=False, blank=False)
    cve = models.ManyToManyField(CVE)
```

- /api/vulns/references
- /api/vulns/references/${id}
- /api/vulns/references/${id}/cves - same idki

---

## Refsource

```python
class Refsource(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False, unique=True)
    reference = models.ManyToManyField(Reference)
```

- /api/vulns/refsources
- /api/vulns/refsources/${id}
- /api/vulns/refsources/${id}/references

---

## Tag

```python
class Tag(models.Model):
    name = models.CharField(max_length=20, null=False, blank=False, unique=True)
    reference = models.ManyToManyField(Reference)
```

- /api/vulns/tags
- /api/vulns/tags/${id}
- /api/vulns/tags/${id}/references

---

---

# CPEMatch

```python
class CPEMatch(models.Model):
    cve = models.ManyToManyField(CVE)
    is_vulnerable = models.BooleanField()
    uri = models.CharField(max_length=512, null=False, blank=False)

```

- /api/vulns/cpemtaches
- /api/vulns/cpemtaches/${id}
- /api/vulns/cpemtaches/${id}/cves

---

---

# Vector

```python
class Vector(models.Model):
    vector = models.CharField(max_length=44, blank=False, null=False, unique=True)

```

- /api/vulns/vectors
- /api/vulns/vectors/${id}
- /api/vulns/vectors/${id}/cves byłoby miło idki

---

---

# CVSSV2, baseMetricV2

## CVSSV2

```python
class CVSSV2(models.Model):
    vector = models.ForeignKey(Vector, on_delete=models.CASCADE, null=False, blank=False)
    version = models.DecimalField(max_digits=5, decimal_places=2, null=False, blank=False)
    access_vector = models.CharField(max_length=20, choices=ACCESS_VECTOR)
    access_complexity = models.CharField(max_length=20, choices=ACCESS_COMPLEXITY)
    authentication = models.CharField(max_length=20, choices=AUTHENTICATION)
    confidentiality_impact = models.CharField(max_length=20, choices=CONFIDENTIALITY_IMPACT)
    integrity_impact = models.CharField(max_length=20, choices=INTEGRITY_IMPACT)
    availability_impact = models.CharField(max_length=20, choices=AVAIALABILITY_IMPACT)
    base_score = models.DecimalField(max_digits=5, decimal_places=2, null=False, blank=False)
```

- /api/vulns/cvssv2s/ wszsytkie cvssv2
- /api/vulns/cvssv2s/${id} konkretne cvssv2
- /api/vulns/cvssv2s/${id}/vectors same vectory idki

---

## baseMetricV2

```python
class BaseMetricV2(models.Model):
    cve = models.ManyToManyField(CVE, null=True, blank=True)
    cvss_v2 = models.ForeignKey(CVSSV2, on_delete=models.CASCADE, null=True, blank=True)
    severity = models.CharField(max_length=20, choices=SEVERITY)
    exploitability_score = models.DecimalField(max_digits=5, decimal_places=2, null=False, blank=False)
    impact_score = models.DecimalField(max_digits=5, decimal_places=2, null=False, blank=False)
    is_obtain_all_privilege  = models.BooleanField()
    is_obtain_user_privilege = models.BooleanField()
    is_obtain_other_privilege = models.BooleanField()
    is_user_interaction_required = models.BooleanField(default=None, blank=True, null=True)
```

- /api/vulns/basemetricv2s/ wszsytkie baseMetricV2 lista, cześć danych
- /api/vulns/basemetricv2s/${id} konkrentne ze szczegółami
- /api/vulns/basemetricv2s/${id}/cvssv2s same idki
- /api/vulns/basemetricv2s/${id}/cves same idki

---

---

# CVSSV3, baseMetricV3

## CVSSV3
```python
class CVSSV3(models.Model):
    version = models.DecimalField(max_digits=5, decimal_places=2, null=False, blank=False)
    vector = models.ForeignKey(Vector, on_delete=models.CASCADE, null=False, blank=False)
    attack_vector = models.CharField(max_length=20, choices=ATTACK_VECTOR)
    attack_complexity = models.CharField(max_length=20,choices=ATTACK_COMPLEXITY)
    privileges_required = models.CharField(max_length=20, choices=PRIVILEGES_REQUIRED)
    user_interaction = models.CharField(max_length=20, choices=USER_INTERACTION)
    scope = models.CharField(max_length=20, choices=SCOPE, null=True)
    confidentiality_impact = models.CharField(max_length=20, choices=CONFIDENTIALITY_IMPACT)
    integrity_impact = models.CharField(max_length=20, choices=INTEGRITY_IMPACT)
    availability_impact = models.CharField(max_length=20, choices=AVAIALABILITY_IMPACT)
    base_score = models.DecimalField(max_digits=5, decimal_places=2, null=False, blank=False)
    base_severity = models.CharField(max_length=20, choices=BASE_SEVERITY)
```

- /api/vulns/CVSSV3s lista
- /api/vulns/CVSSV3s/${id} konkrenty ze szczegółami
- /api/vulns/CVSSV3s/${id}/vectors same idki

---
## BaseMetricV3

```python
class BaseMetricV3(models.Model):
    cve = models.ManyToManyField(CVE)
    cvss_v3 = models.ForeignKey(CVSSV3, on_delete=models.CASCADE)
    exploitability_score = models.DecimalField(max_digits=5, decimal_places=2, null=False, blank=False)
    impact_score = models.DecimalField(max_digits=5, decimal_places=2, null=False, blank=False)
```

- /api/vulns/BaseMetricV3s lista
- /api/vulns/BaseMetricV3s/${id} konkrenty ze szczegółami
- /api/vulns/BaseMetricV3s/${id}/cves same idki lista
- /api/vulns/BaseMetricV3s/${id}/cvssv3s same idki lista

---