from django.contrib import admin

from apps.vulnerabilities import models

admin.site.register(models.CWE)
admin.site.register(models.CVE)
admin.site.register(models.Vector)
admin.site.register(models.Reference)
admin.site.register(models.CPE)
