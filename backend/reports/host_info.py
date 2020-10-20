from fpdf import FPDF, HTMLMixin
import json
import requests
class PDF(FPDF, HTMLMixin):
    def header(self):
        self.set_font('Arial', 'B', 16)

    def headerOnlyFirstSide(self):
        self.image('../../logo.png',90,15, 30)
        self.cell(0, 100, 'Host adress: 46.29.18.78', 0, 0, 'C')
        self.ln(60)

    def chapter(self):
        response = requests.get("http://127.0.0.1:8000/search/censys/46.29.18.78")
        searchDomainInfo = json.loads(response.text)
        epw = pdf.w - 2*pdf.l_margin
        col_width = epw/3
        firstColumnTable = [['Protocols port',
                'host: '+str(searchDomainInfo["protocols_port"]["http"][0]),
                'imaps: '+str(searchDomainInfo["protocols_port"]["imaps"][0]),
                'smtp: '+str(searchDomainInfo["protocols_port"]["smtp"][0])+", "+str(searchDomainInfo["protocols_port"]["smtp"][1])+", " +str(searchDomainInfo["protocols_port"]["smtp"][2]),
                'pop3s: '+str(searchDomainInfo["protocols_port"]["pop3s"][0]),
                'pop3: '+str(searchDomainInfo["protocols_port"]["pop3"][0]),
                'ftp: '+str(searchDomainInfo["protocols_port"]["ftp"][0]),
                'imap: '+str(searchDomainInfo["protocols_port"]["imap"][0]),
                'https: '+str(searchDomainInfo["protocols_port"]["https"][0]),
                'banner: '+str(searchDomainInfo["protocols_port"]["banner"][0])+', '+str(searchDomainInfo["protocols_port"]["banner"][1])+', '+str(searchDomainInfo["protocols_port"]["banner"][2]),
                'Longitude: '+str(searchDomainInfo["longitude"])]]
        self.set_font('Times','',12.0) 
        self.ln(0.5)
        th = pdf.font_size

        for row in firstColumnTable:
            top = pdf.y
            for datum in row:
                offset = pdf.x + col_width
                self.multi_cell(col_width, 1.6*th, str(datum),0,0,'L')
            self.ln(2*th)


        SecondColumnTable = [['Latitude:  '+str(searchDomainInfo["latitude"]),
                'Timezone: '+str(searchDomainInfo["timezone"]),
                'Continent: '+str(searchDomainInfo["continent"]),
                'Registered country: '+str(searchDomainInfo["registered_country"]['PL']),
                'Description: '+str(searchDomainInfo["description"]),
                'RIR: '+str(searchDomainInfo["rir"]),
                'Routed prefix: '+str(searchDomainInfo["routed_prefix"])]]
        self.set_font('Times','',12.0) 
        self.ln(0.5)
        th2 = pdf.font_size
       
        for row in SecondColumnTable:
            pdf.y = top
            for datum in row:
                pdf.x = offset               
                self.multi_cell(col_width, 1.6*th, str(datum),0,0,'L')
            self.ln(2*th2)


        ThirdColumnTable = [['Path: '+str(searchDomainInfo["path"]),
                'ASN: '+str(searchDomainInfo["asn"]),
                'Name: '+str(searchDomainInfo["name"]),
                'DNS names: '+str(searchDomainInfo["dns_names"]),
                'DNS errors: '+str(searchDomainInfo["dns_erros"]),
                'OS: '+str(searchDomainInfo["os"]),
                'Updated at: '+str(searchDomainInfo["updated_at"])]]
        self.ln(0.5)
        self.set_font('Times','',12.0) 
        for row in ThirdColumnTable:
            pdf.y = top
            for datum in row:
                pdf.x = offset+col_width               
                self.multi_cell(col_width, 1.6*th, str(datum),0,0,'L')
            self.ln(2*th2)
        self.ln(20)


        
        FirstColumnTable2 = [['Web page title: '+str(searchDomainInfo["https"]["webpage_title"]),
                'Web page body SHA256: '+str(searchDomainInfo["https"]["webpage_body_sha256"]),
                'Status code: '+str(searchDomainInfo["https"]["status_code"]),
                'Metadata',
                'Product: '+str(searchDomainInfo["https"]["get_metadata"]["product"]),
                'Version: '+str(searchDomainInfo["path"]),
                'Description: '+str(searchDomainInfo["path"]),
                'Manufacturer: '+str(searchDomainInfo["path"])]]

        self.set_font('Times','',12.0) 

        self.ln(0.5)
        th = pdf.font_size

        for row in FirstColumnTable2:
            top = pdf.y
            for datum in row:
                offset = pdf.x + col_width
                self.multi_cell(col_width, 1.6*th, str(datum),0,0,'L')
            self.ln(2*th)



        SecondColumnTable2 = [['RSA export: '+str(searchDomainInfo["https"]["rsa_export"]),
                'RSA length: '+str(searchDomainInfo["https"]["rsa_length"]),
                'RSA modulus: '+str(searchDomainInfo["https"]["rsa_modulus"]),
                'RSA exponent: '+str(searchDomainInfo["https"]["rsa_exponent"]),
                'DHE export: '+str(searchDomainInfo["https"]["dhe_export"]),
                'DH params',
                'Prime length: '+str(searchDomainInfo["https"]["dh_params"]["prime_length"]),
                'Prime value: '+str(searchDomainInfo["https"]["dh_params"]["prime_value"]),
                'Generator length: '+str(searchDomainInfo["https"]["dh_params"]["generator_length"])]]
        self.set_font('Times','',12.0) 

        self.ln(0.5)
        th2 = pdf.font_size
       
        for row in SecondColumnTable2:
            pdf.y = top
            for datum in row:
                pdf.x = offset               
                self.multi_cell(col_width, 1.6*th, str(datum),0,0,'L')
            self.ln(2*th2)


        ThirdColumnTable2 = [['Generator value: '+str(searchDomainInfo["https"]["dh_params"]["generator_value"]),
                'DHE support: '+str(searchDomainInfo["https"]["dhe_support"]),
                'Heartbleed: '+str(searchDomainInfo["https"]["heartbleed"]),
                'Logjam attack: '+str(searchDomainInfo["https"]["logjam_attack"]),
                'Freak attack: '+str(searchDomainInfo["https"]["freak_attack"]),
                'Poodle attack: '+str(searchDomainInfo["https"]["poodle_attack"])
                ]]
        self.set_font('Times','',12.0) 
        self.ln(0.5)
        th2 = pdf.font_size      
        for row in ThirdColumnTable2:
            pdf.y = top
            for datum in row:
                pdf.x = offset+col_width               
                self.multi_cell(col_width, 1.6*th, str(datum),0,0,'L')
            self.ln(2*th2)


        self.ln(450)
    

        Table3 = [['Tbs noct fingerprint: '+str(searchDomainInfo["https"]["tls"]["chain"][0]["tbs_noct_fingerprint"]),
                'Subject DN: '+str(searchDomainInfo["https"]["tls"]["chain"][0]["subject_dn"]),
                'Common name: '+str(searchDomainInfo["https"]["tls"]["chain"][0]["common_name"][0]),
                'Organization: '+str(searchDomainInfo["https"]["tls"]["chain"][0]["organization"][0]),
                'Organizational unit: '+str(searchDomainInfo["https"]["tls"]["chain"][0]["organizational_unit"]),
                'Signature algorithm oid: '+str(searchDomainInfo["https"]["tls"]["chain"][0]["signature_algorithm_oid"]),
                'Signature algorithm name: '+str(searchDomainInfo["https"]["tls"]["chain"][0]["signature_algorithm_name"]),
                'Redacted: '+str(searchDomainInfo["https"]["tls"]["chain"][0]["redacted"]),
                'Serial number: '+str(searchDomainInfo["https"]["tls"]["chain"][0]["serial_number"]),
                'alidation level: '+str(searchDomainInfo["https"]["tls"]["chain"][0]["validation_level"]),
                'Issuer DN: '+str(searchDomainInfo["https"]["tls"]["chain"][0]["issuer_dn"]),
                'Fingerprint SHA1: '+str(searchDomainInfo["https"]["tls"]["chain"][0]["fingerprint_sha1"]),
                'Version: '+str(searchDomainInfo["https"]["tls"]["chain"][0]["version"]),
                'Fingerprint SHA256: '+str(searchDomainInfo["https"]["tls"]["chain"][0]["fingerprint_sha256"]),
                'TBS fingerprint: '+str(searchDomainInfo["https"]["tls"]["chain"][0]["tbs_fingerprint"]),
                'Names '+str(searchDomainInfo["https"]["tls"]["chain"][0]["names"]),
                'Validity start: '+str(searchDomainInfo["https"]["tls"]["chain"][0]["validity_start"]),
                'Validity valid: '+str(searchDomainInfo["https"]["tls"]["chain"][0]["validity_valid"]),
                'Validity start: '+str(searchDomainInfo["https"]["tls"]["chain"][0]["validity_value"]),
                'Fingerprint MD5: '+str(searchDomainInfo["https"]["tls"]["chain"][0]["fingerprint_md5"]),
                'Spki subject fingerprint: '+str(searchDomainInfo["https"]["tls"]["chain"][0]["spki_subject_fingerprint"]),
                'Subject key info fingerprint SHA256: '+str(searchDomainInfo["https"]["tls"]["chain"][0]["subject_key_info_fingerprint_sha256"]),
                'Subject key info fingerprint algorithm name: '+str(searchDomainInfo["https"]["tls"]["chain"][0]["subject_key_info_key_algorithm_name"]),
                'Subject key info fingerprint RSA public key length: '+str(searchDomainInfo["https"]["tls"]["chain"][0]["subject_key_info_rsa_public_key_lenght"]),
                'Subject key info fingerprint RSA public key modulus:  '+str(searchDomainInfo["https"]["tls"]["chain"][0]["subject_key_info_rsa_public_key_modulus"]),
                'Subject key info fingerprint RSA public key exponent: '+str(searchDomainInfo["https"]["tls"]["chain"][0]["subject_key_info_rsa_public_key_exponent"]),
                'Signature self signed: '+str(searchDomainInfo["https"]["tls"]["chain"][0]["signature_self_signed"]),
                'Signature valid: '+str(searchDomainInfo["https"]["tls"]["chain"][0]["signature_valid"]),
                'Signature value: '+str(searchDomainInfo["https"]["tls"]["chain"][0]["signature_value"]),
                'Issuer organizational unit: '+str(searchDomainInfo["https"]["tls"]["chain"][0]["issuer_organizational_unit"]),
                'Issuer common name: '+str(searchDomainInfo["https"]["tls"]["chain"][0]["issuer_common_name"][0]),
                'ssuer organization: '+str(searchDomainInfo["https"]["tls"]["chain"][0]["issuer_organization"][0]),
                'Extensions',
                'Authority key ID: '+str(searchDomainInfo["https"]["tls"]["chain"][0]["extensions"]["authority_key_id"]),
                'Certificate policies cps: '+str(searchDomainInfo["https"]["tls"]["chain"][0]["extensions"]["certificate_policies_cps"]),
                'Certificate policies ID: '+str(searchDomainInfo["https"]["tls"]["chain"][0]["extensions"]["certificate_policies_id"]),
                'Authority info access ocsp urls: '+str(searchDomainInfo["https"]["tls"]["chain"][0]["extensions"]["authority_info_access_ocsp_urls"]),
                'Authority info access issuer urls: '+str(searchDomainInfo["https"]["tls"]["chain"][0]["extensions"]["authority_info_access_issuer_urls"]),
                'Client auth: '+str(searchDomainInfo["https"]["tls"]["chain"][0]["extensions"]["client_auth"]),
                'Server auth: '+str(searchDomainInfo["https"]["tls"]["chain"][0]["extensions"]["server_auth"]),
                'DNS names: '+str(searchDomainInfo["https"]["tls"]["chain"][0]["extensions"]["dns_names"]),
                'IS CA: '+str(searchDomainInfo["https"]["tls"]["chain"][0]["extensions"]["is_ca"]),
                'CRL distribution points: '+str(searchDomainInfo["https"]["tls"]["chain"][0]["extensions"]["crl_distribution_points"]),
                'Key usage key encipherment: '+str(searchDomainInfo["https"]["tls"]["chain"][0]["extensions"]["key_usage_key_encipherment"]),
                'Key usage value: '+str(searchDomainInfo["https"]["tls"]["chain"][0]["extensions"]["key_usage_value"]),
                'Key usage is digital signature: '+str(searchDomainInfo["https"]["tls"]["chain"][0]["extensions"]["key_usage_is_digital_signature"]),
                'Subject key ID: '+str(searchDomainInfo["https"]["tls"]["chain"][0]["extensions"]["subject_key_id"])]]
        self.set_font('Times','',12.0) 
        self.ln(0.5)
        th = pdf.font_size

        for row in Table3:
            top = pdf.y
            for datum in row:
                self.multi_cell(epw, 1.6*th, str(datum),0,0,'L')
                
    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')
        self.rect(7, 7, 196, 283)
        self.rect(5, 5, 200, 287)
        


pdf = PDF()
pdf.alias_nb_pages()
pdf.add_page()
pdf.headerOnlyFirstSide()
pdf.chapter()
pdf.set_font('Times', '', 12)
pdf.output('report_host_info.pdf', 'F')