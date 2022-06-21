from pyexpat import model
from typing import List, Dict, Optional

from apps.vulnerabilities import models

def get_cwe_by_id(cwe_id:str)->Optional[models.CWE]:
    cwe_obj = None

    try:
        if cwe_id:
            if 'NVD-CWE-Other' in cwe_id:
                cwe_obj = models.CWE.objects.get(id='NVD-CWE-Other')
            else:
                cwe_id = cwe_id.replace('CWE-', '') 
                cwe_obj = models.CWE.objects.get(id=cwe_id)
    except models.CWE.DoesNotExist:
        pass

    return cwe_obj

def get_and_save_cve(id:str, published:str, modified:str, description:str, cwe_id:str)->Optional[models.CVE]:
    cve_obj = None
    try:
        id = id.replace('CVE-', '')
        cve_obj = models.CVE.objects.get(id=id)
    except models.CVE.DoesNotExist:
        pass

    cwe_obj = get_cwe_by_id(cwe_id)
    if not cve_obj:
        id = id.replace('CVE-', '')
        cve_obj, _ = models.CVE.objects.get_or_create(
            id=id, 
            published=published[:10], #['“1999-12-30T05:00Z”
            modified=modified[:10], 
            description=description,
            )
        if cwe_obj and cve_obj:
                cve_obj.cwe = cwe_obj

        cve_obj.save()
    return cve_obj