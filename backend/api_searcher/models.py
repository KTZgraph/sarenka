""""
Modele potrzebne do przechowywania danych relacji CWE - do CVE.
Problem - mamy informacje o kodzie CWE w CVE ale relacja w drugą stronę nie jest nigdzie
na stronie https://nvd.nist.gov/ ani https://cwe.mitre.org/.
"""
from django.db import models


class CWEDate(models.Model):
    """Zapisuje w bazie datę pliku z którego pochodza kody CWE"""
    timestamp = models.CharField(max_length=100, default="")


class CWEModel(models.Model):
    """Klasa do przechowywanie kodów CWE (common weakness enumeration)
    ogólnych słabości np.: SQL Injection i listy konkretnych podatnosci CVE związanych z nim.
    Relacja 1 one (CWE) <- n many (CVE) """
    cwe_id = models.CharField(max_length=15, unique=True)
    title = models.TextField() # może być długi opis

    def __str__(self):
        return f"CWE_ID: {self.cwe_id}\n title: {self.title}"


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
