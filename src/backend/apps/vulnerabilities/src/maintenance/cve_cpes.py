from apps.vulnerabilities import models

def save_cpe_list(cpe_list, cve_obj):
    for cpe in cpe_list:
        cpe_obj, _ = models.CPEMatch.objects.get_or_create(
            uri=cpe.get('uri'),
            is_vulnerable=cpe.get('is_vulnerable')
        )

        if cpe_obj and cve_obj:
            cpe_obj.cve.set([cve_obj])

        #save obj to database
        cpe_obj.save()
