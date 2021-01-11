from common.dict_x import DictX
from common.common import Common


class TLSCertificateExtensionsWrapper:
    def __init__(self, data):
        self.data = data.get("extensions", {})

    @property
    def authority_key_id(self):
        return self.data.get("authority_key_id")

    ###########################
    # certificate_policies
    @property
    def ceritificate_policies(self):
        # Czy tworzyć na sztywno słowniki z wszystkimi możlwiymi kluczami?
        return self.data.get("certificate_policies", {})

    @property
    def certificate_policies_cps(self):
        cps = [i.get("cps") for i in self.ceritificate_policies if i.get("cps")]
        return Common.list_flattening(cps) # moze byc pusta lista

    @property
    def certificate_policies_id(self):
        ids = [i.get("id") for i in self.ceritificate_policies]
        return ids # moze byc pusta lista

    #####################################
    # authority_info_access
    @property
    def authority_info_access_ocsp_urls(self):
        return self.data.get("authority_info_access", {}).get("ocsp_urls")

    @property
    def authority_info_access_issuer_urls(self):
        return self.data.get("authority_info_access", {}).get("issuer_urls")

    #####################################
    # extended_key_usage
    @property
    def client_auth(self):
        return self.data.get("extended_key_usage", {}).get("client_auth")

    @property
    def server_auth(self):
        return self.data.get("extended_key_usage", {}).get("server_auth")

    #####################################
    # subject_alt_names
    @property
    def dns_names(self):
        return self.data.get("subject_alt_names", {}).get("dns_names")

    #####################################
    # basic_constraints
    @property
    def is_ca(self):
        return self.data.get("basic_constraints", {}).get("is_ca")

    #####################################
    @property
    def crl_distribution_points(self):
        return self.data.get("crl_distribution_points")


    #####################################
    # key_usage
    @property
    def key_usage_key_encipherment(self):
        return self.data.get("key_usage", {}).get("key_encipherment")

    @property
    def key_usage_value(self):
        return self.data.get("key_usage", {}).get("value")

    @property
    def key_usage_is_digital_signature(self):
        return self.data.get("key_usage", {}).get("digital_signature")

    @property
    def subject_key_id(self):
        return self.data.get("subject_key_id")

    @property
    def to_json(self):
        response = {}

        response.update({"authority_key_id": self.authority_key_id})
        response.update({"certificate_policies_cps": self.certificate_policies_cps})
        response.update({"certificate_policies_id": self.certificate_policies_id})
        response.update({"authority_info_access_ocsp_urls": self.authority_info_access_ocsp_urls})
        response.update({"authority_info_access_issuer_urls": self.authority_info_access_issuer_urls})
        response.update({"client_auth": self.client_auth})
        response.update({"server_auth": self.server_auth})
        response.update({"dns_names": self.dns_names})
        response.update({"is_ca": self.is_ca})
        response.update({"crl_distribution_points": self.crl_distribution_points})
        response.update({"key_usage_key_encipherment": self.key_usage_key_encipherment})
        response.update({"key_usage_value": self.key_usage_value})
        response.update({"key_usage_is_digital_signature": self.key_usage_is_digital_signature})
        response.update({"subject_key_id": self.subject_key_id})

        return response

    def __str__(self):
        return Common.dict_to_string(self.to_json)


class TLSCertificateWrapper:
    def __init__(self, data):
        self.data = data
        self.__extensions = TLSCertificateExtensionsWrapper(self.data.get("parsed", {}))

    @property
    def extensions(self):
        return self.__extensions.to_json
    
    @property
    def tbs_noct_fingerprint(self):
        return self.data.get("parsed", {}).get("tbs_noct_fingerprint")

    @property
    def subject_dn(self):
        return self.data.get("parsed", {}).get("subject_dn")

    @property
    def common_name(self):
        return self.data.get("parsed", {}).get("subject", {}).get("common_name")

    @property
    def organization(self):
        return self.data.get("parsed", {}).get("subject", {}).get("organization")

    @property
    def organizational_unit(self):
        return self.data.get("parsed", {}).get("subject", {}).get("organizational_unit")

    @property
    def signature_algorithm_oid(self):
        """
        https://crypto.stackexchange.com/questions/63157/who-assigns-algorithm-oids-for-cryptographic-algorithms
        """
        return self.data.get("parsed", {}).get("signature_algorithm", {}).get("oid")

    @property
    def signature_algorithm_name(self):
        return self.data.get("parsed", {}).get("signature_algorithm", {}).get("name")

    @property
    def redacted(self):
        return self.data.get("parsed", {}).get("redacted")

    @property
    def serial_number(self):
        return self.data.get("parsed", {}).get("serial_number")

    @property
    def validation_level(self):
        """
        https://www.ssl.com/article/dv-ov-and-ev-certificates/
        DV Certificates - Domain validated 
        OV Certificates - Organization validated
        EV Certificates - Extended validation
        """
        level = self.data.get("parsed", {}).get("validation_level", "").lower()
        switcher = {
            "dv": "domain",
            "ov": "organization",
            "ev": "extended",
            "unknown": "no data",
            "": None
        }

        return switcher.get(level)

    @property
    def issuer_dn(self):
        return self.data.get("parsed", {}).get("issuer_dn")

    @property
    def fingerprint_sha1(self):
        return self.data.get("parsed", {}).get("fingerprint_sha1")

    @property
    def version(self):
        return self.data.get("parsed", {}).get("version")

    @property
    def fingerprint_sha256(self):
        return self.data.get("parsed", {}).get("fingerprint_sha256")

    @property
    def tbs_fingerprint(self):
        return self.data.get("parsed", {}).get("tbs_fingerprint")

    @property
    def names(self):
        result = self.data.get("parsed", {}).get("names")
        return result

    ######################
    # validity
    @property
    def validity(self):
        result = self.data.get("parsed", {}).get("validity", {})
        return result

    @property
    def validity_start(self):
        return self.validity.get("start")
    
    @property
    def validity_valid(self):
        return self.validity.get("valid")

    @property
    def validity_value(self):
        return self.validity.get("value")

    @property
    def fingerprint_md5(self):
        return self.data.get("parsed", {}).get("fingerprint_md5")

    @property
    def spki_subject_fingerprint(self):
        return self.data.get("parsed", {}).get("spki_subject_fingerprint")

    ######################
    # subject key info
    @property
    def subject_key_info_fingerprint_sha256(self):
        return self.data.get("parsed", {}).get("subject_key_info", {}).get("fingerprint_sha256")

    @property
    def subject_key_info_key_algorithm_name(self):
        return self.data.get("parsed", {}).get("subject_key_info", {}).get("key_algorithm", {}).get("name")

    @property
    def subject_key_info_rsa_public_key_lenght(self):
        return self.data.get("parsed", {}).get("subject_key_info", {}).get("rsa_public_key", {}).get("length")

    @property
    def subject_key_info_rsa_public_key_modulus(self):
        return self.data.get("parsed", {}).get("subject_key_info", {}).get("rsa_public_key", {}).get("modulus")

    @property
    def subject_key_info_rsa_public_key_exponent(self):
        return self.data.get("parsed", {}).get("subject_key_info", {}).get("rsa_public_key", {}).get("exponent")


    ######################
    # signature 
    @property
    def signature_self_signed(self):
        return self.data.get("parsed", {}).get("signature", {}).get("self_signed")

    @property
    def signature_valid(self):
        return self.data.get("parsed", {}).get("signature", {}).get("valid")

    @property
    def signature_value(self):
        return self.data.get("parsed", {}).get("signature", {}).get("value")

    @property
    def signature_signature_algorithm_oid(self):
        """
        https://crypto.stackexchange.com/questions/63157/who-assigns-algorithm-oids-for-cryptographic-algorithms
        """
        return self.data.get("parsed", {}).get("signature", {}).get("signature_algorithm", {}).get("oid")

    @property
    def signature_signature_algorithm_name(self):
        return self.data.get("parsed", {}).get("signature", {}).get("signature_algorithm", {})

    ######################
    # issuer
    @property
    def issuer_organizational_unit(self):
        return self.data.get("parsed", {}).get("issuer", {}).get("organizational_unit")

    @property
    def issuer_common_name(self):
        return self.data.get("parsed", {}).get("issuer", {}).get("common_name")

    @property
    def issuer_organization(self):
        return self.data.get("parsed", {}).get("issuer", {}).get("organization")

    @property
    def to_json(self):
        response = {}
        response.update({"tbs_noct_fingerprint": self.tbs_noct_fingerprint})
        response.update({"subject_dn": self.subject_dn})
        response.update({"common_name": self.common_name})
        response.update({"organization": self.organization})
        response.update({"organizational_unit": self.organizational_unit})
        response.update({"signature_algorithm_oid": self.signature_algorithm_oid})
        response.update({"signature_algorithm_name": self.signature_algorithm_name})
        response.update({"redacted": self.redacted})
        response.update({"serial_number": self.serial_number})
        response.update({"validation_level": self.validation_level})
        response.update({"issuer_dn": self.issuer_dn})
        response.update({"fingerprint_sha1": self.fingerprint_sha1})
        response.update({"version": self.version})
        response.update({"fingerprint_sha256": self.fingerprint_sha256})
        response.update({"tbs_fingerprint": self.tbs_fingerprint})
        response.update({"names": self.names})
        
        ######################
        #validity
        response.update({"validity_start": self.validity_start})
        response.update({"validity_valid": self.validity_valid})
        response.update({"validity_value": self.validity_value})


        response.update({"fingerprint_md5": self.fingerprint_md5})
        response.update({"spki_subject_fingerprint": self.spki_subject_fingerprint})

        ######################
        # subject key info
        response.update({"subject_key_info_fingerprint_sha256": self.subject_key_info_fingerprint_sha256})
        response.update({"subject_key_info_key_algorithm_name": self.subject_key_info_key_algorithm_name})
        response.update({"subject_key_info_rsa_public_key_lenght": self.subject_key_info_rsa_public_key_lenght})
        response.update({"subject_key_info_rsa_public_key_modulus": self.subject_key_info_rsa_public_key_modulus})
        response.update({"subject_key_info_rsa_public_key_exponent": self.subject_key_info_rsa_public_key_exponent})

        ######################
        # signature 
        response.update({"signature_self_signed": self.signature_self_signed})
        response.update({"signature_valid": self.signature_valid})
        response.update({"signature_value": self.signature_value})

        ######################
        # issuer
        response.update({"issuer_organizational_unit": self.issuer_organizational_unit})
        response.update({"issuer_common_name": self.issuer_common_name})
        response.update({"issuer_organization": self.issuer_organization})

        # extensions
        response.update({"extensions": self.extensions})

        return response

    def __str__(self):
        response = "\n\n----------------------------TLSCertificateWrapper\n"
        response += Common.dict_to_string(self.to_json)
        return response


class TLSWrapper:
    def __init__(self, data):
        self.data = DictX(data)
        self.__certificate = TLSCertificateWrapper(self.data.get("certificate", {}))
        self.__chain = self.__get_chain()

    def __get_chain(self):
        result = []
        for chain in self.data.get("chain"):
            result.append(
                TLSCertificateWrapper(chain).to_json
            )

        return result

    @property
    def chain(self):
        return self.__chain

    @property
    def certificate(self):
        return self.__certificate

    @property
    def version(self):
        return self.data.get("version")

    @property
    def dh_params(self):
        return self.data.get("server_key_exchange", {}).get("dh_params")
        
    @property
    def dh_prime(self):
        response = {"prime_length": None, "prime_value": None}
        prime = self.data.get("dh_params", {}).get("prime", {})
        if prime:
            response["prime_length"] = prime.get("length")
            response["prime_value"] = prime.get("value")
        return response

    @property
    def dh_generator(self):
        response = {"generator_lenght": None, "generator_value": None}
        generator = self.data.get("dh_params", {}).get("generator", {})
        if generator:
            response["generator_lenght"] = generator.get("length")
            response["generator_value"] = generator.get("value")
        return response

    @property
    def cipher_suite(self):
        return self.data.get("cipher_suite", {})

    @property
    def cipher_suite_id(self):
        return self.cipher_suite.get("id")

    @property
    def cipher_suite_name(self):
        return self.cipher_suite.get("name")

    @property
    def session_ticket_length(self):
        return self.data.get("session_ticket", {}).get("length")

    @property
    def ocsp_stapling(self):
        return self.data.get("ocsp_stapling")

    @property
    def signature_valid(self):
        return self.data.get("singature", {}).get("valid")

    @property
    def validation(self):
        return self.data.get("validation", {})

    @property
    def validation_browser_trusted(self):
        return self.validation.get("browser_trusted")

    @property
    def validation_browser_error(self):
        return self.validation.get("browser_error")

    @property
    def to_json(self):
        result = {}
        result.update({"chain": self.chain})
        result.update({"certificate": self.certificate})
        result.update({"version": self.version})
        result.update({"cipher_suite_id": self.cipher_suite_id})
        result.update({"cipher_suite_name": self.cipher_suite_name})
        result.update({"dh_prime": self.dh_prime})
        result.update({"dh_generator": self.dh_generator})
        result.update({"session_ticket_length": self.session_ticket_length})
        result.update({"ocsp_stapling": self.ocsp_stapling})
        result.update({"validation_browser_trusted": self.validation_browser_trusted})
        result.update({"validation_browser_error": self.validation_browser_error})
        result.update({"certificate": self.certificate.extensions})

        return result
    
    def __str__(self):
        return Common.dict_to_string(self.to_json)
