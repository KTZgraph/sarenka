from apps.vulnerabilities import models

# ------------ BASE METRIC V2 -------------------
def save_cvss_v2(cvss_v2):
    cvss_v2_obj, _ = models.CVSSV2.objects.get_or_create(
        version= cvss_v2.get("version"),
        access_vector= cvss_v2.get("access_vector"),
        access_complexity= cvss_v2.get("access_complexity"),
        authentication= cvss_v2.get("authentication"),
        confidentiality_impact= cvss_v2.get("confidentiality_impact"),
        integrity_impact= cvss_v2.get("integrity_impact"),
        availability_impact= cvss_v2.get("availability_impact"),
        base_score= int(cvss_v2.get("base_score")),
    )
    # Vector
    if cvss_v2.get("vector"):
        vector_obj, _ = models.Vector.objects.get_or_create(
            vector = cvss_v2.get("vector")
        )
        if vector_obj and cvss_v2_obj:
            cvss_v2_obj.vector = vector_obj

    # save and return object
    cvss_v2_obj.save()
    return cvss_v2_obj

def save_base_metric_v2(base_metric_v2, cve_obj):

    base_metric_v2_obj, _ = models.BaseMetricV2.objects.get_or_create(
        severity=base_metric_v2.get("severity"),
        exploitability_score=int(base_metric_v2.get("exploitability_score")[0]), #TODO
        impact_score= int(base_metric_v2.get("impact_score")[0]), #TODO
        is_obtain_all_privilege=base_metric_v2.get("is_obtain_all_privilege")[0], #TODO
        is_obtain_user_privilege=base_metric_v2.get("is_obtain_user_privilege")[0], #TODO
        is_obtain_other_privilege=base_metric_v2.get("is_obtain_other_privilege")[0], #TODO
        is_user_interaction_required=base_metric_v2.get("is_user_interaction_required")[0], #TODO
    )

    if base_metric_v2_obj and cve_obj:
        base_metric_v2_obj.cve.set([cve_obj])
    
    cvss_v2_obj = save_cvss_v2(base_metric_v2.get('cvss_v2'))
    if base_metric_v2_obj and cvss_v2_obj:
        base_metric_v2_obj.cvss_v2 = cvss_v2_obj

    base_metric_v2_obj.save()

# ------------ BASE METRIC V3 -------------------
def save_cvss_v3(cvss_v3):
    cvss_v3_obj, _ = models.CVSSV3.objects.get_or_create(
        version = cvss_v3.get('version'),
        attack_vector = cvss_v3.get('attack_vector'),
        attack_complexity = cvss_v3.get('attack_complexity'),
        privileges_required = cvss_v3.get('privileges_required'),
        user_interaction = cvss_v3.get('user_interaction'),
        scope = cvss_v3.get('scope'),
        confidentiality_impact = cvss_v3.get('confidentiality_impact'),
        integrity_impact = cvss_v3.get('integrity_impact'),
        availability_impact = cvss_v3.get('availability_impact'),
        base_score = cvss_v3.get('base_score'),
        base_severity = cvss_v3.get('base_severity')
    )

    # Vector
    vector_obj, _ = models.Vector.objects.get_or_create(
        vector = cvss_v3.get("vector")
    )
    if vector_obj and cvss_v3_obj:
        cvss_v3_obj.vector = vector_obj

    # save and return object
    cvss_v3_obj.save()
    return cvss_v3_obj

def save_base_metric_v3(base_metric_v3, cve_obj):
    cvss_v3_obj = save_cvss_v3(base_metric_v3.get('cvss_v3'))
    base_metric_v3_obj, _ = models.BaseMetricV3.objects.get_or_create(
        exploitability_score = int(base_metric_v3.get('exploitability_score')),
        impact_score = int(base_metric_v3.get('impact_score')),
    )

    if base_metric_v3_obj and cvss_v3_obj:
        base_metric_v3_obj.cvss_v3 = cvss_v3_obj

    if base_metric_v3_obj and cve_obj:
        base_metric_v3_obj.cve = cve_obj
    
    base_metric_v3_obj.save()
