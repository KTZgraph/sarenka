import json
from django.shortcuts import render
from django.http import HttpResponse

from connectors.credential import Credential
from connectors.cve_search.connector import Connector

def get_by_cve(request, id="CVE-2010-3333"):
    credentials = Credential().cve_search
    connector = Connector(credentials)
    response = connector.search_by_cve_code("CVE-2010-3333")
    
    return HttpResponse(json.dumps(response.to_dict()))