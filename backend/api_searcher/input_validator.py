import re

class InputValidator:
    @staticmethod
    def is_cve_code(data):
        if re.match("CVE-\d{4}-\d+", data):
            return True
        return False
