from typing import List, Dict, Optional

from apps.vulnerabilities import models


def get_and_save_cve(id:str, published:str, modified:str, description:str, cwe_id:str)->Optional[models.CVE]:
    print('------------ get_and_save_cve -----------')
    cwe_obj = None
    cve_obj = None
    try:
        id = id.replace('CVE-', '')
        cve_obj = models.CVE.objects.get(id=id)
    except models.CVE.DoesNotExist:
        pass

    try:
        if cwe_id:
            if 'NVD-CWE-Other' in cwe_id:
                cwe_obj = models.CWE.objects.get(id=cwe_id)
            else:
                cwe_id = cwe_id.replace('CWE-', '') 
                cwe_obj = models.CWE.objects.get(id=cwe_id)
    except models.CWE.DoesNotExist:
        pass
    
    if not cve_obj:
        id = id.replace('CVE-', '')
        cve_obj = models.CVE.objects.create(
            id=id, 
            published=published[:10], #['“1999-12-30T05:00Z”
            modified=modified[:10], 
            description=description,
            )
        if cwe_obj:
            # Direct assignment to the forward side of a many-to-many set is prohibited. Use cve.set() instead.
            cve_obj.cwe.set(cwe_obj)

        cve_obj.save()
    return cve_obj