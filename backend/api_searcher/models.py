""""
Modele potrzebne do przechowywania danych relacji CWE - do CVE.
Problem - mamy informacje o kodzie CWE w CVE ale relacja w drugą stronę nie jest nigdzie
na stronie https://nvd.nist.gov/ ani https://cwe.mitre.org/.
"""
from django.db import models


class CWEModel(models.Model):
    """Klasa do przechowywanie kodów CWE (common weakness enumeration)
    ogólnych słabości np.: SQL Injection i listy konkretnych podatnosci CVE związanych z nim.
    Relacja 1 one (CWE) <- n many (CVE)
    "ID_CWE": "CWE-79",
    "title": "Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting')",
    "description": "The software does not neutralize or incorrectly neutralizes user-controllable input before it is placed in output that is used as a web page that is served to other users. ",
    "likehood": "High",
    "technical_impact": [
        "Read Application Data",
        "Bypass Protection Mechanism",
        "Execute Unauthorized Code or Commands"
    ],
    "caused_by": {
        "field": "Architecture and Design",
        "process": "Implementation",
        "description": "This weakness is caused during implementation of an architectural security tactic."
    },
    """
    cwe_id = models.CharField(max_length=15, unique=True)
    title = models.TextField() # może być długi opis
    description = models.TextField() # może być długi opis
    likehood = models.TextField(max_length=100)

    def __str__(self):
        return f"CWE_ID: {self.cwe_id}\n title: {self.title}"


class TechnicalImactModel(models.Model):
    """
    1 (one) CWE <- n (many) impacts
    "technical_impact": [
        "Bypass Protection Mechanism",
        "Read Application Data",
        "Execute Unauthorized Code or Commands"
    ],
    """

    title = models.TextField()


class CausedByModel(models.Model):
    """
    1 (one) CWE <- n (many) CausedByModel
    "caused_by": {
        "field": "Architecture and Design",
        "process": "Implementation",
        "description": "This weakness is caused during implementation of an architectural security tactic."
    },
    """
    field = models.CharField(max_length=350)
    process = models.TextField(max_length=350)
    description = models.TextField()


class CVEModel(models.Model):
    """Common Vulnerabilities and Exposures (CVE) - konkretna podatnośc z konkretnej wersji oprogramowania.
    CVE-\d{4}-\d{4,7}
    Relacja n many (CVE) -> 1 one (CWE)  """
    cve_id  = models.CharField(max_length=17, unique=True)
    year = models.CharField(max_length=4)
    month = models.CharField(max_length=2) # miesiące cyframi 1,2, ..., 12
    cwe = models.ForeignKey(CWEModel,
                            on_delete=models.CASCADE,
                            related_name="cwe_model")

    def __str__(self):
        return f"CVE_ID: {self.cve}\n year: {self.year} \n month: {self.month}"
