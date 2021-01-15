from fpdf import FPDF, HTMLMixin
import json
import requests


class PDFHostInfo(FPDF, HTMLMixin):
    # TODO wywalic to !!!!!!!!!!!!!


    def header(self):
        self.set_font('Arial', 'B', 16)


    def headerOnlyFirstSide(self,ipAdress):
        # self.image('logo.png',90,15, 30)
        self.cell(0, 10, 'Host adress: '+ipAdress, 0, 0, 'C')
        self.ln(10)


    def chapter(self, ipAdress,link):
        #GET JSON
        response = requests.get(link+ipAdress)
        searchDomainInfo = json.loads(response.text)
        epw = self.w - 2*self.l_margin
        col_width = epw/3
        self.set_font('Times','',12.0)
        th = self.font_size



        #FIRST COLUMN - FITST TABLE - TITLE
        self.ln(10)
        self.set_font('Times','B',16.0) 
        top = self.y
        self.set_text_color(192,11,38)
        self.cell(col_width,self.font_size, 'PROTOCOLS PORT', 0, 0, 'L')
        self.ln(10)
        self.set_text_color(0,0,0)
        self.set_font('Times','',12.0)



        #FIRST COLUMN - FITST TABLE - TEXT
        for key in searchDomainInfo["protocols_port"]:
            self.multi_cell(col_width, 1.6*th, str(key)+": "+(', '.join(map(str,searchDomainInfo["protocols_port"][key]))),0,0,'L')
        offset = self.x + col_width



        #SECOND COLUMN - FITST TABLE - TITLE
        self.set_font('Times','B',16.0) 
        self.y = top
        self.x = offset
        self.set_text_color(192,11,38)
        self.cell(col_width,self.font_size, 'DETAILS', 0, 0, 'L')
        self.ln(10)



        #SECOND COLUMN - FITST TABLE - TEXT
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



        #THIRD COLUMN - FITST TABLE - TITLE
        self.set_font('Times','B',16.0) 
        self.y = top
        self.x = offset+col_width
        self.set_text_color(192,11,38)
        self.cell(col_width,self.font_size, 'DETAILS', 0, 0, 'L')
        self.ln(10)



        #THIRD COLUMN - FITST TABLE - TEXT
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



        #FIRST COLUMN - SECOND TABLE - TITLE        
        self.ln(20)
        self.set_font('Times','B',16.0) 
        top = self.y
        self.set_text_color(192,11,38)
        self.cell(col_width,self.font_size, 'METADATA', 0, 0, 'L')
        self.ln(10)
        


        #FIRST COLUMN - SECOND TABLE - TEXT        
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




        #FIRST COLUMN - SECOND TABLE - TITLE        
        self.ln(10)
        self.set_font('Times','B',16.0) 
        self.set_text_color(192,11,38)
        self.cell(col_width,self.font_size, 'DH PARAMS', 0, 0, 'L')
        self.ln(10)
        
        
        
        #FIRST COLUMN - SECOND TABLE - TEXT        
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
    


        #SECOND COLUMN - SECOND TABLE - TITLE        
        self.set_font('Times','B',16.0) 
        self.y = top
        self.x = offset  
        self.set_text_color(192,11,38)
        self.cell(col_width,self.font_size, 'DETAILS HTTPS', 0, 0, 'L')
        self.ln(10)


      
        #SECOND COLUMN - SECOND TABLE - TEXT        
        self.set_font('Times','',12.0)
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
                self.multi_cell(col_width, 1.6*th,(text+str(text2)),0,0,'L')

    

        #THIRD COLUMN - SECOND TABLE - TITLE        
        self.set_font('Times','B',16.0) 
        self.y = top
        self.x = offset+col_width
        self.set_text_color(192,11,38)
        self.cell(col_width,self.font_size, 'DETAILS HTTPS', 0, 0, 'L')
        self.ln(10)



        #THIRD COLUMN - SECOND TABLE - TEXT        
        self.set_font('Times','',12.0) 
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
                self.multi_cell(col_width, 1.6*th,(text+str(text2)),0,0,'L')

        self.ln(450)




        #THIRD TABLE - TITLE        
        self.ln(10)
        self.set_font('Times','B',18.0) 
        self.set_text_color(192,11,38)
        self.cell(0, 20, 'TLS CERTIFICATE CHAIN', 0, 0, 'C')
        self.ln(20)

        
        
        #THIRD TABLE - TEXT        
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
                self.multi_cell(epw, 1.6*th,(text+str(text2)),0,0,'L')



        #FOURTH TABLE - TITLE        
        self.set_font('Times','B',18.0) 
        self.ln(10)
        self.set_text_color(192,11,38)
        self.cell(0, 20, 'EXTENSIONS', 0, 0, 'C')
        self.ln(20)
        


        #FOURTH TABLE - TEXT        
        self.set_font('Times','',12.0) 
        self.ln(0.5)
        th = self.font_size
        top = self.y
        for key in  searchDomainInfo["https"]["tls"]["chain"][0]["extensions"]:
            text=str(key).replace("_", " ").capitalize()+": "
            text2=searchDomainInfo["https"]["tls"]["chain"][0]["extensions"][key]
            if(isinstance(text2, list)):
                self.set_text_color(0, 0, 0)
                self.multi_cell(epw, 1.6*th, str(text+(', '.join(map(str,text2)))),0,0,'L')
            else:               
                if(str(text2)=='None'):
                    self.set_text_color(179, 179, 179)
                else:
                    self.set_text_color(0, 0, 0)
                self.multi_cell(epw, 1.6*th,(text+str(text2)),0,0,'L')



    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.set_text_color(0,0,0)
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')
        self.rect(7, 7, 196, 283)
        self.rect(5, 5, 200, 287)
        