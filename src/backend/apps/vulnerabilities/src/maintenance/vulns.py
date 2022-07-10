import os
import json
from django.conf import settings
from apps.vulnerabilities import models
from rzodkiewka.rzodkiewka import save_info

CWE_OUTPUT_FILEPATH = os.path.join(settings.BASE_DIR, "output", "cwe.json")
CVE_OUTPUT_FOLDER = os.path.join(settings.BASE_DIR, "cve_output")

def get_cwes():
    print(CWE_OUTPUT_FILEPATH)
    with open(CWE_OUTPUT_FILEPATH, "r", encoding='utf-8') as f:
        data = json.loads(f.read())
    return data

def save_cwes_db(): # "time": "0:00:09.008696"
    cwe_list = get_cwes()
    for cwe in cwe_list:
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
    pass


def save_db():
    # save_info() # "time": "0:05:45.715412"
    save_cwes_db() # "time": "0:00:09.008696"
    save_cves_db()