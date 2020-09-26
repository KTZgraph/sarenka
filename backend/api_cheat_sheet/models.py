from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class NoDataChoice(models.TextChoices):
    NOT_SET = (0, "0")
    UNABLE_TO_DETECT = (-1, "-1")
    NONPUBLIC = (-2, "-2")


class CWEModel(models.Model):
    """
    Klasa przechowujaca informacje o ogólnym typie podntości
    np. SQL Injection które występuje w różnych orpogramowanaich i różnych wersja
    definicje sparsowane z https://cwe.mitre.org/data/definitions/23.html
    Najczęstsze https://cwe.mitre.org/top25/archive/2020/2020_cwe_top25.html
    """
    RANK = tuple([(i, str(i)) for i in range(1,26)])

    code = models.PositiveSmallIntegerField(unique=True)
    description = models.TextField()
    attack_example = models.TextField(null=True, default=None)
    cve_example = models.CharField(max_length=20, null=True, default=None)
    tutorial_example = models.CharField(max_length=200, null=True, default=None)
    top_25 = models.BooleanField(default=False)# https://cwe.mitre.org/top25/archive/2020/2020_cwe_top25.html
    rank = models.CharField(
        max_length=2,
        null=True,
        default=NoDataChoice.NOT_SET,
        choices=RANK
        )

    @property
    def has_example(self):
        return self.tutorial_example is not None

    @property
    def has_tutorial(self):
        return self.tutorial_example is not None

    @property
    def has_attack(self):
        return self.attack_example is not None

