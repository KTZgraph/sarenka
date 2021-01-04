from common.dict_x import DictX
from .tls_wrapper import TLSWrapper
from common.common import Common


class HTTPSWrapper:
    def __init__(self, data):
        self.data = DictX(data)
        self.__tls = self.get_tls()

    @property
    def status_code(self):
        get_data = self.data.get("get")
        return get_data.get("status_code")

    @property
    def get_metadata(self):
        """
        Data from https://censys.io/ipv4/50.56.73.47
        dla Apache httpd 2.2.17 https://www.cvedetails.com/vulnerability-list/vendor_id-45/product_id-66/version_id-109443/Apache-Http-Server-2.2.17.html
        https://www.netcompliancesolutions.com/.htaccess  - sprawdizć czy jest ta ściezka - jeśli tak tomamy apache 
        """
        get_data = self.data.get("get", {})
        metadata = get_data.get("metadata")
        response = {"product": None, "version" : None, "description": None, "manufacturer": None }
        if metadata:
            response["product"] = metadata.get("product")
            response["version"] = metadata.get("version")
            response["description"] = metadata.get("description")
            response["manufacturer"] = metadata.get("manufacturer")

        return response

    @property
    def webpage_title(self):
        """
        Webpage title
        """
        get_data = self.data.get("get", {})
        title = get_data.get("title")
        return title

    @property
    def webpage_body_sha256(self):
        """
        Webpage body_sha256
        """
        get_data = self.data.get("get", {})
        body_sha256 = get_data.get("body_sha256")
        return body_sha256

    @property
    def heartbleed(self):
        info = self.data.get("heartbleed", {})
        if info.get("heartbeat_enabled") or info.get("heartbleed_vulnerable"):
            return True
        
        return False

    @property
    def rsa_export(self):
        return self.data.rsa_export.get("support")

    @property
    def rsa_params(self):
        rsa_params = self.data.rsa_export.get("rsa_params")

        response = {"lenght" : None, "modulus": None, "exponent": None}
        if rsa_params:
            response["lenght"] = rsa_params.get("lenght")
            response["modulus"] = rsa_params.get("modulus")
            response["exponent"] = rsa_params.get("exponent")

        return response

    @property
    def rsa_length(self):
        return self.rsa_params.get("length")
    
    @property
    def rsa_modulus(self):
        return self.rsa_params.get("modulus")

    @property
    def rsa_exponent(self):
        return self.rsa_params.get("exponent")

    @property
    def ssl_3_support(self):
        return self.data.get("ssl_3", {}).get("support")

    @property
    def dhe_export(self):
        """
        https://crypto.stackexchange.com/questions/33859/what-is-dhe-export-cipher-suite
        """
        return self.data.dhe_export.get("support")

    @property
    def dh_params(self):
        dh = self.data.dhe_export.get("dh_params")
        response = {"prime_length": None, "prime_value": None, "generator_length": None, "generator_value": None}
        if dh:
            response["prime_length"] = dh.get("prime", {}).get("lenght")
            response["prime_value"] = dh.get("prime", {}).get("value")
            response["generator_length"] = dh.get("generator", {}).get("lenght")
            response["generator_value"] = dh.get("generator", {}).get("value")

        return response

    @property
    def dhe_support(self):
        return self.data.dhe.get("support")

    @property
    def logjam_attack(self):
        """
        https://weakdh.org/
        Export DHE True -> This host is vulnerable to the Logjam attack.
        """
        return self.rsa_export

    @property
    def freak_attack(self):
        """
        Export RSA True  -> This host is vulnerable to the FREAK attack.
        """
        return self.dhe_export

    @property
    def poodle_attack(self):
        """
        SSLv3 Support True -> This host is vulnerable to the POODLE attack.
        """
        return self.ssl_3_support

    def get_tls(self):
        return TLSWrapper(self.data.tls).to_json

    @property
    def tls(self):
        return self.__tls

    @property
    def to_json(self):
        result = {}
        result.update({"status_code":self.status_code})
        result.update({"get_metadata":self.get_metadata})
        result.update({"heartbleed":self.heartbleed})
        result.update({"rsa_export":self.rsa_export})
        result.update({"rsa_length":self.rsa_length})
        result.update({"rsa_modulus":self.rsa_modulus})
        result.update({"rsa_exponent":self.rsa_exponent})
        result.update({"dhe_export":self.dhe_export})
        result.update({"dh_params":self.dh_params})
        result.update({"dhe_support":self.dhe_support})
        result.update({"logjam_attack":self.logjam_attack})
        result.update({"freak_attack":self.freak_attack})
        result.update({"poodle_attack":self.poodle_attack})
        result.update({"poodle_attack":self.poodle_attack})
        result.update({"webpage_title":self.webpage_title})
        result.update({"webpage_body_sha256":self.webpage_body_sha256})
        result.update({"tls":self.tls})

        return result

    def __str__(self):
        return Common.dict_to_string(self.to_json)
