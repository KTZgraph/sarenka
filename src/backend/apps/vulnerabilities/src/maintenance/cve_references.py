from typing import Optional
from apps.vulnerabilities import models

def save_references_list(references_list:dict, cve_obj:Optional[models.CVE]=None):
        for reference in references_list:
            reference_obj, _ = models.Reference.objects.get_or_create(
                name=reference.get("name"),
                url=reference.get("url"),
            )

            # add cve to reference_obj
            if reference_obj and cve_obj:
                reference_obj.cve.set([cve_obj])

            #create refsource refsource": "MISC",
            refsource_obj, _ = models.Refsource.objects.get_or_create(
                name = reference.get("refsource")
            )

            if reference_obj and refsource_obj:
                refsource_obj.reference.set([reference_obj])
            refsource_obj.save()

            #tags "references_list": [ "tags": []
            for tag_name in reference.get("tags"):
                tag_obj, _ =models.Tag.objects.get_or_create(
                    name=tag_name
                )
                if tag_obj and refsource_obj:
                    tag_obj.reference.set([reference_obj])
                #save tag obj
                tag_obj.save()
