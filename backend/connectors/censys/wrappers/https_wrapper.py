from common.dict_x import DictX
from wrappers.tls_wrapper import TLSWrapper

class HTTPSWrapper:
    def __init__(self, data):
        self.data = DictX(data)
        self.tls = self.get_tls()

    @property
    def status_code(self):
        get_data = self.data.get("get")
        return get_data.get("status_code")

    @property
    def heartbleed(self):
        info = self.data.heartbleed
        if info.get("heartbeat_enabled") or info.get("heartbleed_vulnerable"):
            return True
        
        return False

    @property
    def rsa_export(self):
        return self.data.rsa_export.get("support")

    @property
    def dhe_export(self):
        """
        https://crypto.stackexchange.com/questions/33859/what-is-dhe-export-cipher-suite
        """
        return self.data.dhe_export.get("support")

    @property
    def dhe_support(self):
        return self.data.dhe.get("support")

    @property
    def logjam(self):
        """
        https://weakdh.org/
        """
        return "Not implemented"

    def get_tls(self):
        return TLSWrapper(self.data.tls)

    def __str__(self):
        return f"Status:{self.status_code}\nHeartbleed:{self.heartbleed}\nRSA export:{self.rsa_export}\nDHE export:{self.dhe_export}\nDHE support:{self.dhe_support}"
    