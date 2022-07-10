import os
import json

from django.conf import settings
from apps.vulnerabilities import models
from rzodkiewka.rzodkiewka import save_info #TODO

from apps.vulnerabilities.src.maintenance.cve_references import save_references_list
from apps.vulnerabilities.src.maintenance.cve_base_metric import save_base_metric_v2, save_base_metric_v3
from apps.vulnerabilities.src.maintenance.cve_cpes import save_cpe_list
from apps.vulnerabilities.src.maintenance.cwe_missed import missed_cve_list


CWE_OUTPUT_FILEPATH = os.path.join(settings.BASE_DIR, "output", "cwe.json")
CVE_OUTPUT_FILEPATH = os.path.join(settings.BASE_DIR, "cve_output", "CWE-1.json")
# CVE_OUTPUT_FOLDER = os.path.join(settings.BASE_DIR, "cve_output")
CVE_ALL_FILEPATH= os.path.join(settings.BASE_DIR, "output", "cve.json")

class VulnsCWEError(Exception):
    def __init__(self, msg=None, errors=None) -> None:
        super().__init__(msg)
        self.errors = errors

def save_cwes_db(): # "time": "0:00:09.008696"
    with open(CWE_OUTPUT_FILEPATH, "r", encoding='utf-8') as f:
        cwe_list = json.loads(f.read())

    for cwe in cwe_list:
        models.CWE.objects.get_or_create(
            code = f'CWE-{cwe.get("id")}',
            name = cwe.get("name"),
            abstraction = cwe.get("abstraction"),
            structure = cwe.get("structure"),
            status = cwe.get("status"),
            description = cwe.get("description"),
            extended_description = cwe.get("extended_description")
        )

def save_missed_cwes()->list[str]:
    with open(CWE_OUTPUT_FILEPATH, "r", encoding='utf-8') as f:
        cwe_list = json.loads(f.read())
    cwe_ids = [f'CWE-{cwe.get("id")}' for cwe in cwe_list]
    cwe_ids += [cwe.get("id") for cwe in missed_cve_list]
    cwe_ids = set(cwe_ids)

    with open(CVE_ALL_FILEPATH, "r", encoding='utf-8') as f:
        cve_list_all = json.loads(f.read())
    cve_cwe_ids_set = set([cve.get('cwe_id') for cve in cve_list_all])

    cwe_ids_diff = cve_cwe_ids_set - cwe_ids
    if cwe_ids_diff:
        raise VulnsCWEError(f"No data: {cwe_ids_diff}")

    for cwe in missed_cve_list:
        models.CWE.objects.get_or_create(
            code = cwe.get("id"),
            name = cwe.get("name"),
            abstraction = cwe.get("abstraction"),
            structure = cwe.get("structure"),
            status = cwe.get("status"),
            description = cwe.get("description"),
            extended_description = cwe.get("extended_description")
        )

def save_cves_db():
    with open(CVE_OUTPUT_FILEPATH, "r", encoding='utf-8') as f:
        cve_list = json.loads(f.read())

    for cve in cve_list:
        cwe_obj = models.CWE.objects.get(code=cve.get('cwe_id'))
        version_obj, _ = models.Version.objects.get_or_create(version = cve.get('version'))
        assigner_obj, _ = models.Assigner.objects.get_or_create(email= cve.get('assigner'))
        format_obj, _ = models.Format.objects.get_or_create(format=cve.get("data_format"))

        # save CVE objects
        cve_obj, _ = models.CVE.objects.get_or_create(
            cwe = cwe_obj,
            version = version_obj,
            assigner = assigner_obj,
            format = format_obj,
            code = cve.get('cve_id'),
            published =cve.get("published")[:10],
            modified = cve.get("modified")[:10],
            description = cve.get("description"),

        )
        # save references to db
        save_references_list(references_list=cve.get("references_list"), cve_obj=cve_obj)

        # "CVE-2022-1983" "base_metric_v2" "base_metric_v3"
        save_base_metric_v2(cve.get("base_metric_v2"), cve_obj)
        
        # base_metric_v2
        save_base_metric_v3(cve.get("base_metric_v3"), cve_obj)
        
        # "CVE-2022-1983" "cpe_list": [
        save_cpe_list(cve.get("cpe_list"), cve_obj)
        
        # save cve objects
        cve_obj.save()

def save_db():
    # save_info() # "time": "0:05:45.715412"
    # TODO: write it in 'rzodkiewka'
    save_cwes_db() # "time": "0:00:09.008696"
    save_missed_cwes()
    # save_cves_db()