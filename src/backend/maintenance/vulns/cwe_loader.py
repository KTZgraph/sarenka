import json
import os

from apps.vulnerabilities.models import CWE

class CWELoader:
    _cwe_file = ""