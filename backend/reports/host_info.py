from fpdf import FPDF, HTMLMixin
import json
import requests



class PDF(FPDF, HTMLMixin):


    def header(self):
        self.set_font('Arial', 'B', 16)


    def headerOnlyFirstSide(self,ipAdress):
        self.image('../logo.png',90,15, 30)
        self.cell(0, 100, 'Host adress: '+ipAdress, 0, 0, 'C')
        self.ln(60)


    def chapter(self, ipAdress,link):
        response = requests.get(link+ipAdress)
        searchDomainInfo = json.loads(response.text)
        epw = self.w - 2*self.l_margin
        col_width = epw/3
        self.set_font('Times','',12.0)
        th = self.font_size

        # json_dictionary = json.loads([searchDomainInfo["protocols_port"]])

        # firstColumnTable = [['Protocols port',
        #         'host: '+str(searchDomainInfo["protocols_port"]),
        #         'imaps: '+str(searchDomainInfo["protocols_port"]),
        #         'smtp: '+str(searchDomainInfo["protocols_port"]),
        #         'pop3s: '+str(searchDomainInfo["protocols_port"]),
        #         'pop3:'+str(searchDomainInfo["protocols_port"]),
        #         'ftp: '+str(searchDomainInfo["protocols_port"]),
        #         'imap: '+str(searchDomainInfo["protocols_port"]),
        #         'https: '+str(searchDomainInfo["protocols_port"]),
        #         'banner:'+str(searchDomainInfo["protocols_port"]),
        #         'Longitude:'+str(searchDomainInfo["protocols_port"])]]
        # for key in searchDomainInfo["protocols_port"]:
        #     print(key, ":", searchDomainInfo["protocols_port"][key])

        # firstColumnTable = [
        #         #'Protocols port',
        #         # for key in searchDomainInfo["protocols_port"]:
        #         #     print(key, ":", searchDomainInfo["protocols_port"][key])
        #         # for key in json_dictionary:
        #         #     print(key, ":", json_dictionary[key])
        #         # 'host: '+str(searchDomainInfo["protocols_port"]),
        #         # 'imaps: '+str(searchDomainInfo["protocols_port"]),
        #         # 'smtp: '+str(searchDomainInfo["protocols_port"]),
        #         # 'pop3s: '+str(searchDomainInfo["protocols_port"]),
        #         # 'pop3:'+str(searchDomainInfo["protocols_port"]),
        #         # 'ftp: '+str(searchDomainInfo["protocols_port"]),
        #         # 'imap: '+str(searchDomainInfo["protocols_port"]),
        #         # 'https: '+str(searchDomainInfo["protocols_port"]),
        #         # 'banner:'+str(searchDomainInfo["protocols_port"]),
        #         # 'Longitude:'+str(searchDomainInfo["protocols_port"])
        #         ]


        self.ln(10)
        self.set_font('Times','B',16.0) 
        top = self.y
        self.set_text_color(192,11,38)
        self.cell(col_width,self.font_size, 'PROTOCOLS PORT', 0, 0, 'L')
        self.ln(10)
        self.set_text_color(0,0,0)
        self.set_font('Times','',12.0)

        for key in searchDomainInfo["protocols_port"]:
            # print(key, ":", searchDomainInfo["protocols_port"][key])
            self.multi_cell(col_width, 1.6*th, str(key)+": "+(', '.join(map(str,searchDomainInfo["protocols_port"][key]))),0,0,'L')
        offset = self.x + col_width
            # firstColumnTable.append(
            #     str(key)+": "+(', '.join(map(str,searchDomainInfo["protocols_port"][key])))
            #     )
        # print(firstColumnTable)
        # self.set_text_color(0,0,0)
        # self.set_font('Times','',12.0) 
        # self.ln(0.5)
        # th = self.font_size
        # # top = self.y
        # for row in firstColumnTable:
        #     # top = self.y


        #     # for datum in row:
        #     offset = self.x + col_width
        #     self.multi_cell(col_width, 1.6*th, str(row),0,0,'L')
        #     # for datum in row:
        #     #     offset = self.x + col_width
        #     #     self.multi_cell(col_width, 1.6*th, str(datum),0,0,'L')
        #     # self.ln(th)

        #         # self.y = top


        # self.x = offset 
        self.set_font('Times','B',16.0) 

        self.y = top
        self.x = offset
        # self.x = offset  
        self.set_text_color(192,11,38)
        self.cell(col_width,self.font_size, 'DETAILS', 0, 0, 'L')
        self.ln(10)

        # SecondColumnTable = [
        #         # 'Latitude:  '+str(searchDomainInfo["latitude"]),
        #         # 'Timezone: '+str(searchDomainInfo["timezone"]),
        #         # 'Continent: '+str(searchDomainInfo["continent"])
        #         # 'Registered country: '+str(searchDomainInfo["registered_country"]),
        #         # 'Description: '+str(searchDomainInfo["description"]),
        #         # 'RIR: '+str(searchDomainInfo["rir"]),
        #         # 'Routed prefix: '+str(searchDomainInfo["routed_prefix"])
        #         ]
        # for key in  searchDomainInfo["registered_country"]:
        #     SecondColumnTable.append(str(key)+": "+str(searchDomainInfo["registered_country"][key]))

        # SecondColumnTable.append('Description: '+str(searchDomainInfo["description"]))
        # SecondColumnTable.append('RIR: '+str(searchDomainInfo["rir"]))
        # SecondColumnTable.append('Routed prefix: '+str(searchDomainInfo["routed_prefix"]))
        SecondColumnTableItem=['longitude','latitude','timezone','continent','registered_country','description', 'rir', 'routed_prefix']

        self.set_font('Times','',12.0)        
        for key in  searchDomainInfo:
            text=str(key).replace("_", " ").capitalize()+": "
            text2=searchDomainInfo[key]
            self.x = offset   
            if(isinstance(text2, list) and key in SecondColumnTableItem ):
                self.set_text_color(0, 0, 0)
                self.multi_cell(col_width, 1.6*th, str(text+(', '.join(map(str,text2)))),0,0,'L')                         
            elif(key in SecondColumnTableItem ):
                if(str(text2)=='None'):
                        self.set_text_color(179, 179, 179)
                else:
                    self.set_text_color(0, 0, 0)
                self.multi_cell(col_width, 1.6*th,(text+str(text2)),0,0,'L')   

        # self.set_text_color(0,0,0)
        # self.set_font('Times','',12.0) 
        # self.ln(0.5)
        # th2 = self.font_size
        # # self.y = top
        # for row in SecondColumnTable:
        #     # top = self.y
        #     # for datum in row:
        #     self.x = offset               
        #     self.multi_cell(col_width, 1.6*th, str(row),0,0,'L')
        #     # self.ln(2*th2)

        self.set_font('Times','B',16.0) 

        self.y = top
        self.x = offset+col_width
        # self.x = offset  
        self.set_text_color(192,11,38)
        self.cell(col_width,self.font_size, 'DETAILS', 0, 0, 'L')
        self.ln(10)

        # ThirdColumnTable = [
        #         # 'Path: '+(', '.join(map(str,searchDomainInfo["path"]))),
        #         # 'ASN: '+str(searchDomainInfo["asn"]),
        #         # 'Name: '+str(searchDomainInfo["name"]),
        #         # 'DNS names: '+str(searchDomainInfo["dns_names"]),
        #         # 'DNS errors: '+str(searchDomainInfo["dns_erros"]),
        #         # 'OS: '+(', '.join(map(str,searchDomainInfo["os"]))),
        #         # 'Updated at: '+str(searchDomainInfo["updated_at"])
        #         ]


        ThirdColumnTableItem=['path','asn','name','dns_names','dns_erros','os', 'updated_at']
        self.set_font('Times','',12.0)
        
        for key in  searchDomainInfo:
            text=str(key).replace("_", " ").capitalize()+": "
            text2=searchDomainInfo[key]
            self.x = offset+col_width               

            if(isinstance(text2, list) and key in ThirdColumnTableItem ):
                self.set_text_color(0, 0, 0)
                self.multi_cell(col_width, 1.6*th, str(text+(', '.join(map(str,text2)))),0,0,'L')                    
            elif(key in ThirdColumnTableItem ):
                if(str(text2)=='None'):
                        self.set_text_color(179, 179, 179)
                else:
                    self.set_text_color(0, 0, 0)
                self.multi_cell(col_width, 1.6*th,(text+str(text2)),0,0,'L')       


            
        # # ThirdColumnTable=[]
        # for key in  searchDomainInfo["path"]:
        #     ThirdColumnTable.append(str(key)+": "+str(searchDomainInfo[key]))
        # print("ll")


        # self.set_text_color(0,0,0)
 
        # self.ln(0.5)
        # self.set_font('Times','',12.0)
        # top= self.y  
        # for row in ThirdColumnTable:
        #     # self.y = top
        #     # for datum in row:
        #     self.x = offset+col_width               
        #     self.multi_cell(col_width, 1.6*th, str(row),0,0,'L')
        #     # self.ln(2*th2)
        
        self.ln(20)

        # self.ln(10)
        self.set_font('Times','B',16.0) 
        top = self.y
        self.set_text_color(192,11,38)
        self.cell(col_width,self.font_size, 'METADATA', 0, 0, 'L')
        self.ln(10)
        
        # FirstColumnTable2 = [
        #         # 'Product: '+str(searchDomainInfo["https"]["get_metadata"]["product"]),
        #         # 'Version: '+str(searchDomainInfo["https"]["get_metadata"]["version"]), 
        #         # 'Description: '+str(searchDomainInfo["https"]["get_metadata"]["description"]),
        #         # 'Manufacturer: '+str(searchDomainInfo["https"]["get_metadata"]["manufacturer"]),
        #         ]
        self.set_font('Times','',12.0)
        for key in  searchDomainInfo["https"]["get_metadata"]:
            text=str(key).replace("_", " ").capitalize()+": "
            text2=searchDomainInfo["https"]["get_metadata"][key]
            offset = self.x + col_width
            if(isinstance(text2, list)):
                self.set_text_color(0, 0, 0)
                self.multi_cell(col_width, 1.6*th, str(text+(', '.join(map(str,text2)))),0,0,'L')             
            else:
                if(str(text2)=='None'):
                        self.set_text_color(179, 179, 179)
                else:
                    self.set_text_color(0, 0, 0)
                self.multi_cell(col_width, 1.6*th,(text+str(text2)),0,0,'L')
        # self.set_text_color(0,0,0)

 

        # self.ln(0.5)
        # th = self.font_size
        # top = self.y
        # for row in FirstColumnTable2:
        #     # top = self.y
        #     # for datum in row:
        #     offset = self.x + col_width
        #     self.multi_cell(col_width, 1.6*th, str(row),0,0,'L')
        # # self.ln(2*th)

        self.ln(10)
        self.set_font('Times','B',16.0) 

        # top = self.y
        # self.y = top -10
        # self.x = offset
        # self.x = offset  
        self.set_text_color(192,11,38)
        self.cell(col_width,self.font_size, 'DH PARAMS', 0, 0, 'L')
        self.ln(10)

        # SecondColumnTable2 = [
        #         # 'Web page title: '+str(searchDomainInfo["https"]["webpage_title"]),
        #         # 'Web page body SHA256: '+str(searchDomainInfo["https"]["webpage_body_sha256"]),
        #         # 'Status code: '+str(searchDomainInfo["https"]["status_code"]),
        #         # 'RSA export: '+str(searchDomainInfo["https"]["rsa_export"]),
        #         # 'RSA length: '+str(searchDomainInfo["https"]["rsa_length"]),
             

        #         # 'DH params',
        #         # 'Prime length: '+str(searchDomainInfo["https"]["dh_params"]["prime_length"]),
        #         # 'Prime value: '+str(searchDomainInfo["https"]["dh_params"]["prime_value"]),
        #         # 'Generator length: '+str(searchDomainInfo["https"]["dh_params"]["generator_length"]),
        #         # 'Generator value: '+str(searchDomainInfo["https"]["dh_params"]["generator_value"]),

        #         ]
        # self.ln(10)
        # self.set_text_color(0,0,0)

        # self.set_font('Times','',12.0) 

        # self.ln(0.5)
        # th2 = self.font_size
        self.set_font('Times','',12.0) 
        for key in  searchDomainInfo["https"]["dh_params"]:
            text=str(key).replace("_", " ").capitalize()+": "
            text2=searchDomainInfo["https"]["dh_params"][key]

            if(isinstance(text2, list) and key!="extensions"):
                self.set_text_color(0, 0, 0)
                self.multi_cell(col_width, 1.6*th, str(text+(', '.join(map(str,text2)))),0,0,'L')                 
            elif(key!="extensions"):
                if(str(text2)=='None'):
                        self.set_text_color(179, 179, 179)
                else:
                    self.set_text_color(0, 0, 0)
                self.multi_cell(col_width, 1.6*th,(text+str(text2)),0,0,'L')
        # for row in SecondColumnTable2:
        #     # self.y = top
        #     # for datum in row:
        #         # self.x = offset   
        #     self.x = offset             
        #         # self.multi_cell(col_width, 1.6*th, str(datum),0,0,'L')
        #     self.multi_cell(col_width, 1.6*th, str(row),0,0,'L')

        # self.ln(2*th2)

        # self.ln(10)
        # self.set_font('Times','B',16.0) 
        # # top = self.y
        # self.set_text_color(192,11,38)
        # self.x = offset    
        # self.y = top         

        # self.cell(col_width,self.font_size, 'DH PARAMS', 0, 0, 'L')
        # self.ln(10)
        # self.set_text_color(0,0,0)

        # self.set_font('Times','',12.0) 

        # self.ln(0.5)
        # th2 = self.font_size

        # for row in SecondColumnTable2:
        #     # self.y = top
        #     # for datum in row:
        #         # self.x = offset   
        #     # self.x = offset             
        #         # self.multi_cell(col_width, 1.6*th, str(datum),0,0,'L')
        #     self.multi_cell(col_width, 1.6*th, str(row),0,0,'L')

        # self.ln(2*th2)







        self.set_font('Times','B',16.0) 

        self.y = top
        # self.x = col_width
        self.x = offset  
        self.set_text_color(192,11,38)
        self.cell(col_width,self.font_size, 'DETAILS HTTPS', 0, 0, 'L')
        self.ln(10)

        # ThirdColumnTable23 = [
        #     #    'Web page title: '+str(searchDomainInfo["https"]["webpage_title"]),
        #     #     'Web page body SHA256: '+str(searchDomainInfo["https"]["webpage_body_sha256"]),
        #     #     'Status code: '+str(searchDomainInfo["https"]["status_code"]),
        #     #     'RSA export: '+str(searchDomainInfo["https"]["rsa_export"]),
        #     #     'RSA length: '+str(searchDomainInfo["https"]["rsa_length"]),
        #     #    'RSA modulus: '+str(searchDomainInfo["https"]["rsa_modulus"]),
        #         # 'RSA exponent: '+str(searchDomainInfo["https"]["rsa_exponent"]),
        #         # 'DHE export: '+str(searchDomainInfo["https"]["dhe_export"]),
        #         # 'DHE support: '+str(searchDomainInfo["https"]["dhe_support"]),
        #         # 'Heartbleed: '+str(searchDomainInfo["https"]["heartbleed"]),
        #         # 'Logjam attack: '+str(searchDomainInfo["https"]["logjam_attack"]),
        #         # 'Freak attack: '+str(searchDomainInfo["https"]["freak_attack"]),
        #         # 'Poodle attack: '+str(searchDomainInfo["https"]["poodle_attack"])
        #         ]


        self.set_font('Times','',12.0)
        # self.x = offset  
        ThirdColumnTable23Item=['webpage_title','webpage_body_sha256','status_code','rsa_export','rsa_length','rsa_modulus']

        for key in  searchDomainInfo["https"]:
            text=str(key).replace("_", " ").capitalize()+": "
            text2=searchDomainInfo["https"][key]
            self.x = offset  
            if(isinstance(text2, list) and key in ThirdColumnTable23Item):
                self.set_text_color(0, 0, 0)
                self.multi_cell(col_width, 1.6*th, str(text+(', '.join(map(str,text2)))),0,0,'L')                 
            elif( key in ThirdColumnTable23Item):
                if(str(text2)=='None'):
                        self.set_text_color(179, 179, 179)
                else:
                    self.set_text_color(0, 0, 0)
                # Table4.append(text+str(text2))
                self.multi_cell(col_width, 1.6*th,(text+str(text2)),0,0,'L')

        
        # self.ln(0.5)
        # th2 = self.font_size 
        # top= self.y   
        # # self.x = offset+col_width  
        # for row in ThirdColumnTable23:
        #     # self.y = top
        #     # for datum in row:
        #     self.x = offset  
        #         # self.multi_cell(col_width, 1.6*th, str(datum),0,0,'L')
        #     self.multi_cell(col_width, 1.6*th, str(row),0,0,'L')
        # self.ln(2*th2)











        self.set_font('Times','B',16.0) 

        self.y = top
        self.x = offset+col_width
        # self.x = offset  
        self.set_text_color(192,11,38)
        self.cell(col_width,self.font_size, 'DETAILS HTTPS', 0, 0, 'L')
        self.ln(10)

        # ThirdColumnTable2 = [
        #     #    'Web page title: '+str(searchDomainInfo["https"]["webpage_title"]),
        #     #     'Web page body SHA256: '+str(searchDomainInfo["https"]["webpage_body_sha256"]),
        #     #     'Status code: '+str(searchDomainInfo["https"]["status_code"]),
        #     #     'RSA export: '+str(searchDomainInfo["https"]["rsa_export"]),
        #     #     'RSA length: '+str(searchDomainInfo["https"]["rsa_length"]),
        #     #    'RSA modulus: '+str(searchDomainInfo["https"]["rsa_modulus"]),
        #         # 'RSA exponent: '+str(searchDomainInfo["https"]["rsa_exponent"]),
        #         # 'DHE export: '+str(searchDomainInfo["https"]["dhe_export"]),
        #         # 'DHE support: '+str(searchDomainInfo["https"]["dhe_support"]),
        #         # 'Heartbleed: '+str(searchDomainInfo["https"]["heartbleed"]),
        #         # 'Logjam attack: '+str(searchDomainInfo["https"]["logjam_attack"]),
        #         # 'Freak attack: '+str(searchDomainInfo["https"]["freak_attack"]),
        #         # 'Poodle attack: '+str(searchDomainInfo["https"]["poodle_attack"])
        #         ]
        self.set_font('Times','',12.0) 
        # self.x = offset+col_width  
        ThirdColumnTable2Item=['rsa_exponent','dhe_export','dhe_support','heartbleed','logjam_attack','freak_attack', 'poodle_attack']

        for key in  searchDomainInfo["https"]:
            text=str(key).replace("_", " ").capitalize()+": "
            text2=searchDomainInfo["https"][key]
            self.x = offset+col_width 
            if(isinstance(text2, list) and key in ThirdColumnTable2Item):
                self.set_text_color(0, 0, 0)
                self.multi_cell(col_width, 1.6*th, str(text+(', '.join(map(str,text2)))),0,0,'L')            
            elif( key in ThirdColumnTable2Item):
                if(str(text2)=='None'):
                        self.set_text_color(179, 179, 179)
                else:
                    self.set_text_color(0, 0, 0)
                # Table4.append(text+str(text2))
                self.multi_cell(col_width, 1.6*th,(text+str(text2)),0,0,'L')

       
        # self.ln(0.5)
        # th2 = self.font_size 
        # top= self.y   
        # # self.x = offset+col_width  
        # for row in ThirdColumnTable2:
        #     # self.y = top
        #     # for datum in row:
        #     self.x = offset+col_width               
        #         # self.multi_cell(col_width, 1.6*th, str(datum),0,0,'L')
        #     self.cell(col_width, 1.6*th, str(row),0,0,'L')
        #     self.ln(th)


        self.ln(450)
    

        # Table3 = [
        #         # 'Tbs noct fingerprint: '+str(searchDomainInfo["https"]["tls"]["chain"][0]["tbs_noct_fingerprint"]),
        #         # 'Subject DN: '+str(searchDomainInfo["https"]["tls"]["chain"][0]["subject_dn"]),
        #         # 'Common name: '+(', '.join(map(str,searchDomainInfo["https"]["tls"]["chain"][0]["common_name"]))),
        #         # 'Organization: '+(', '.join(map(str,searchDomainInfo["https"]["tls"]["chain"][0]["organization"]))),
        #         # 'Organizational unit: '+(', '.join(map(str,searchDomainInfo["https"]["tls"]["chain"][0]["organizational_unit"]))),
        #         # 'Signature algorithm oid: '+str(searchDomainInfo["https"]["tls"]["chain"][0]["signature_algorithm_oid"]),
        #         # 'Signature algorithm name: '+str(searchDomainInfo["https"]["tls"]["chain"][0]["signature_algorithm_name"]),
        #         # 'Redacted: '+str(searchDomainInfo["https"]["tls"]["chain"][0]["redacted"]),
        #         # 'Serial number: '+str(searchDomainInfo["https"]["tls"]["chain"][0]["serial_number"]),
        #         # 'alidation level: '+str(searchDomainInfo["https"]["tls"]["chain"][0]["validation_level"]),
        #         # 'Issuer DN: '+str(searchDomainInfo["https"]["tls"]["chain"][0]["issuer_dn"]),
        #         # 'Fingerprint SHA1: '+str(searchDomainInfo["https"]["tls"]["chain"][0]["fingerprint_sha1"]),
        #         # 'Version: '+str(searchDomainInfo["https"]["tls"]["chain"][0]["version"]),
        #         # 'Fingerprint SHA256: '+str(searchDomainInfo["https"]["tls"]["chain"][0]["fingerprint_sha256"]),
        #         # 'TBS fingerprint: '+str(searchDomainInfo["https"]["tls"]["chain"][0]["tbs_fingerprint"]),
        #         # 'Names '+str(searchDomainInfo["https"]["tls"]["chain"][0]["names"]),
        #         # 'Validity start: '+str(searchDomainInfo["https"]["tls"]["chain"][0]["validity_start"]),
        #         # 'Validity valid: '+str(searchDomainInfo["https"]["tls"]["chain"][0]["validity_valid"]),
        #         # 'Validity start: '+str(searchDomainInfo["https"]["tls"]["chain"][0]["validity_value"]),
        #         # 'Fingerprint MD5: '+str(searchDomainInfo["https"]["tls"]["chain"][0]["fingerprint_md5"]),
        #         # 'Spki subject fingerprint: '+str(searchDomainInfo["https"]["tls"]["chain"][0]["spki_subject_fingerprint"]),
        #         # 'Subject key info fingerprint SHA256: '+str(searchDomainInfo["https"]["tls"]["chain"][0]["subject_key_info_fingerprint_sha256"]),
        #         # 'Subject key info fingerprint algorithm name: '+str(searchDomainInfo["https"]["tls"]["chain"][0]["subject_key_info_key_algorithm_name"]),
        #         # 'Subject key info fingerprint RSA public key length: '+str(searchDomainInfo["https"]["tls"]["chain"][0]["subject_key_info_rsa_public_key_lenght"]),
        #         # 'Subject key info fingerprint RSA public key modulus:  '+str(searchDomainInfo["https"]["tls"]["chain"][0]["subject_key_info_rsa_public_key_modulus"]),
        #         # 'Subject key info fingerprint RSA public key exponent: '+str(searchDomainInfo["https"]["tls"]["chain"][0]["subject_key_info_rsa_public_key_exponent"]),
        #         # 'Signature self signed: '+str(searchDomainInfo["https"]["tls"]["chain"][0]["signature_self_signed"]),
        #         # 'Signature valid: '+str(searchDomainInfo["https"]["tls"]["chain"][0]["signature_valid"]),
        #         # 'Signature value: '+str(searchDomainInfo["https"]["tls"]["chain"][0]["signature_value"]),
        #         # 'Issuer organizational unit: '+str(searchDomainInfo["https"]["tls"]["chain"][0]["issuer_organizational_unit"]),
        #         # 'Issuer common name: '+(', '.join(map(str,searchDomainInfo["https"]["tls"]["chain"][0]["issuer_common_name"]))),
        #         # 'ssuer organization: '+(', '.join(map(str,searchDomainInfo["https"]["tls"]["chain"][0]["issuer_organization"]))),

        #         # 'Extensions',
        #         # 'Authority key ID: '+str(searchDomainInfo["https"]["tls"]["chain"][0]["extensions"]["authority_key_id"]),
        #         # 'Certificate policies cps: '+(', '.join(map(str,searchDomainInfo["https"]["tls"]["chain"][0]["extensions"]["certificate_policies_cps"]))),
        #         # 'Certificate policies ID: '+(', '.join(map(str,searchDomainInfo["https"]["tls"]["chain"][0]["extensions"]["certificate_policies_id"]))),
        #         # 'Authority info access ocsp urls: '+(', '.join(map(str,searchDomainInfo["https"]["tls"]["chain"][0]["extensions"]["authority_info_access_ocsp_urls"]))),
        #         # 'Authority info access issuer urls: '+(', '.join(map(str,searchDomainInfo["https"]["tls"]["chain"][0]["extensions"]["authority_info_access_issuer_urls"]))),
        #         # 'Client auth: '+str(searchDomainInfo["https"]["tls"]["chain"][0]["extensions"]["client_auth"]),
        #         # 'Server auth: '+str(searchDomainInfo["https"]["tls"]["chain"][0]["extensions"]["server_auth"]),
        #         # 'DNS names: '+str(searchDomainInfo["https"]["tls"]["chain"][0]["extensions"]["dns_names"]),
        #         # 'IS CA: '+str(searchDomainInfo["https"]["tls"]["chain"][0]["extensions"]["is_ca"]),
        #         # 'CRL distribution points: '+(', '.join(map(str,searchDomainInfo["https"]["tls"]["chain"][0]["extensions"]["crl_distribution_points"]))),
        #         # 'Key usage key encipherment: '+str(searchDomainInfo["https"]["tls"]["chain"][0]["extensions"]["key_usage_key_encipherment"]),
        #         # 'Key usage value: '+str(searchDomainInfo["https"]["tls"]["chain"][0]["extensions"]["key_usage_value"]),
        #         # 'Key usage is digital signature: '+str(searchDomainInfo["https"]["tls"]["chain"][0]["extensions"]["key_usage_is_digital_signature"]),
        #         # 'Subject key ID: '+str(searchDomainInfo["https"]["tls"]["chain"][0]["extensions"]["subject_key_id"])
        #         ]


        self.ln(10)
        self.set_font('Times','B',18.0) 

        self.set_text_color(192,11,38)
        self.cell(0, 20, 'TLS CERTIFICATE CHAIN', 0, 0, 'C')
        self.ln(20)

        self.set_font('Times','',12.0) 
        self.ln(0.5)

        for key in  searchDomainInfo["https"]["tls"]["chain"][0]:
            text=str(key).replace("_", " ").capitalize()+": "
            text2=searchDomainInfo["https"]["tls"]["chain"][0][key]
            if(isinstance(text2, list) and key!="extensions"):
                self.set_text_color(0, 0, 0)
                self.multi_cell(epw, 1.6*th, str(text+(', '.join(map(str,text2)))),0,0,'L')
                                    

            elif(key!="extensions"):
                if(str(text2)=='None'):
                        self.set_text_color(179, 179, 179)
                else:
                    self.set_text_color(0, 0, 0)
                # Table4.append(text+str(text2))
                self.multi_cell(epw, 1.6*th,(text+str(text2)),0,0,'L')

        # self.set_text_color(0,0,0)
       
        # self.set_font('Times','',12.0) 
        # self.ln(0.5)
        # th = self.font_size
        # top = self.y
        # for row in Table3:
        #     # top = self.y
        #     # for datum in row:
        #         # self.multi_cell(epw, 1.6*th, str(datum),0,0,'L')
        #     self.multi_cell(epw, 1.6*th, str(row),0,0,'L')
        
        self.set_font('Times','B',18.0) 
        self.ln(10)
        self.set_text_color(192,11,38)
        self.cell(0, 20, 'EXTENSIONS', 0, 0, 'C')
        self.ln(20)
        
        
        
        # self.set_text_color(0,0,0)

        self.set_font('Times','',12.0) 
        self.ln(0.5)
        th = self.font_size
        top = self.y
        Table4=[]
        for key in  searchDomainInfo["https"]["tls"]["chain"][0]["extensions"]:
            text=str(key).replace("_", " ").capitalize()+": "
            text2=searchDomainInfo["https"]["tls"]["chain"][0]["extensions"][key]
            if(isinstance(text2, list)):
                # Table4.append(text+(', '.join(map(str,text2))))
                self.set_text_color(0, 0, 0)
                self.multi_cell(epw, 1.6*th, str(text+(', '.join(map(str,text2)))),0,0,'L')
            else:               
                if(str(text2)=='None'):
                    self.set_text_color(179, 179, 179)
                else:
                    self.set_text_color(0, 0, 0)
                # Table4.append(text+str(text2))
                self.multi_cell(epw, 1.6*th,(text+str(text2)),0,0,'L')

                # self.multi_cell(text+str(text2))
            # Table3.append(str(key).replace("_", " ").capitalize()+": "+str(searchDomainInfo["https"]["tls"]["chain"][0]["extensions"][key]))

        # for row in Table4:
        #     # top = self.y
        #     # for datum in row:
        #         # self.multi_cell(epw, 1.6*th, str(datum),0,0,'L')
        #     self.multi_cell(epw, 1.6*th, str(row),0,0,'L')





    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.set_text_color(0,0,0)

        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')
        self.rect(7, 7, 196, 283)
        self.rect(5, 5, 200, 287)
        