from fpdf import FPDF, HTMLMixin

class PDF(FPDF, HTMLMixin):
    def header(self):
        self.set_font('Arial', 'B', 16)


    def chapter(self):
        self.image('../../logo.png',90,15, 30)

        self.cell(0, 100, 'Host adress: 46.29.18.78', 0, 0, 'C')
        self.ln(60)
        
        epw = pdf.w - 2*pdf.l_margin
        col_width = epw/3
        data = [['Protocols port',
        'http: 80',
        'imaps: 993',
        'smtp: 465,25,587',
        'pop3s: 995',
        'pop3: 110',
        'ftp: 21',
        'imap: 143',
        'https: 443',
        'banner: 6666,873',
        'Longitude: 21.0362']]
        self.set_font('Times','',12.0) 
        # self.set_font('Times','',10.0) 
        self.ln(0.5)
        th = pdf.font_size

        for row in data:
            top = pdf.y
            for datum in row:
                offset = pdf.x + col_width
                self.multi_cell(col_width, 1.6*th, str(datum),0,0,'L')
            self.ln(2*th)



        data2 = [['Latitude: 52.2394',
                'Timezone: Europe/Warsaw',
                'Continent: Europe',
                'Registered country: Poland,',
                'Description: SPRINT-SDC',
                'RIR: unknown',
                'Routed prefix: 46.29.16.0/21']]
        self.set_font('Times','',12.0) 
        self.ln(0.5)
        th2 = pdf.font_size
       
        for row in data2:
            pdf.y = top
            for datum in row:
                pdf.x = offset               
                self.multi_cell(col_width, 1.6*th, str(datum),0,0,'L')
            self.ln(2*th2)




        data2 = [['Path: 7018,3257,197226',
                'ASN: 197226',
                'Name: SPRINT-SDC',
                'DNS names: No data available',
                'DNS errors: No data available',
                'OS: No data available',
                'Updated at: 2020-10-11T04:32:48+00:00']]
        self.ln(0.5)
        self.set_font('Times','',12.0) 
        for row in data2:
            pdf.y = top
            for datum in row:
                pdf.x = offset+col_width               
                self.multi_cell(col_width, 1.6*th, str(datum),0,0,'L')
            self.ln(2*th2)
        self.ln(20)







        
        data = [['Web page title: HostingHouse.pl',
                'Web page body SHA256: b9b93998fa0c1b1f3c5da8469bb04254df54cd01060c8e035cfde18ecf1c1181',
                'Status code: 200',
                'Metadata',
                'Product: httpd',
                'Version: No data available',
                'Description: Apache httpd',
                'Manufacturer: Apache']]
        self.set_font('Times','',12.0) 

        self.ln(0.5)
        th = pdf.font_size

        for row in data:
            top = pdf.y
            for datum in row:
                offset = pdf.x + col_width
                self.multi_cell(col_width, 1.6*th, str(datum),0,0,'L')
            self.ln(2*th)



        data2 = [['RSA export: false',
                'RSA length: No data available',
                'RSA modulus: No data available',
                'RSA exponent: No data available',
                'DHE export: false',
                'DH params',
                'Prime length: No data available',
                'Prime value: No data available',
                'Generator length: No data available']]
        self.set_font('Times','',12.0) 

        self.ln(0.5)
        th2 = pdf.font_size
       
        for row in data2:
            pdf.y = top
            for datum in row:
                pdf.x = offset               
                self.multi_cell(col_width, 1.6*th, str(datum),0,0,'L')
            self.ln(2*th2)




        data2 = [['Generator value: No data available',
                'DHE support: true',
                'Heartbleed: true',
                'Logjam attack: false',
                'Freak attack: false',
                'Poodle attack: No data available']]
        self.set_font('Times','',12.0) 
        self.ln(0.5)
        th2 = pdf.font_size      
        for row in data2:
            pdf.y = top
            for datum in row:
                pdf.x = offset+col_width               
                self.multi_cell(col_width, 1.6*th, str(datum),0,0,'L')
            self.ln(2*th2)


        self.ln(450)


        # epw = pdf.w - 2*pdf.l_margin
    

        data = [['Tbs noct fingerprint: 3e1a1a0f6c53f3e97a492d57084b5b9807059ee057ab1505876fd83fda3db838',
                'Subject DN: C=US, O=Lets Encrypt, CN=Lets Encrypt Authority X3',
                'Common name: Lets Encrypt Authority X3',
                'Organization: Lets Encrypt',
                'Organizational unit: No data available',
                'Signature algorithm oid : 1.2.840.113549.1.1.11',
                'Signature algorithm name: SHA256WithRSA',
                'Redacted: false',
                'Serial number: 13298795840390663119752826058995181320',
                'alidation level: domain',
                'Issuer DN: O=Digital Signature Trust Co., CN=DST Root CA X3',
                'Fingerprint SHA1: e6a3b45b062d509b3382282d196efe97d5956ccb',
                'Version: 3',
                'Fingerprint SHA256: 25847d668eb4f04fdd40b12b6b0740c567da7d024308eb6c2c96fe41d9de218d',
                'TBS fingerprint: 3e1a1a0f6c53f3e97a492d57084b5b9807059ee057ab1505876fd83fda3db838',
                'Names: No data available',
                'Validity start: 2016-03-17T16:40:46Z',
                'Validity valid: No data available',
                'Validity start: No data available',
                'Fingerprint MD5: b15409274f54ad8f023d3b85a5ecec5d',
                'Spki subject fingerprint: 78d2913356ad04f8f362019df6cb4f4f8b003be0d2aa0d1cb37d2fd326b09c9e',
                'Subject key info fingerprint SHA256: 60b87575447dcba2a36b7d11ac09fb24a9db406fee12d2cc90180517616e8a18',
                'Subject key info fingerprint algorithm name: RSA']]
        self.set_font('Times','',12.0) 
        self.ln(0.5)
        th = pdf.font_size

        for row in data:
            top = pdf.y
            for datum in row:
                self.multi_cell(epw, 1.6*th, str(datum),0,0,'L')



        data2 = [['Subject key info fingerprint RSA public key length: 2048',
                'Subject key info fingerprint RSA public key modulus: nNMM8FrlLke3cl03g7NoYzDq1zUmGSXhvb418XCSL7e4S0EFq6meNQhY7LEqxGiHC6PjdeTm86dicbp5gWAf15Gan/PQeGdxyGkOlZHP/uaZ6WA8SMx+yk13EiSdRxta67nsHjcAHJyse6cF6s5K671B5TaYucv9bTyWaN8jKkKQDIZ0Z8h/pZq4UmEUEz9l6YKHy9v6Dlb2honzhT+Xhq+w3Brvaw2VFn3EK6BlspkENnWAa6xK8xuQSXgvopZPKiAlKQTGdMDQMc2PMTiVFrqoM7hD8bEfwzB/onkxEz0tNvjj/PIzark5McWvxI0NHWQWM6r6hCm21AvA2H3Dkw==',
                'Subject key info fingerprint RSA public key exponent: 65537',
                'Signature self signed: false',
                'Signature valid: true',
                'Signature value: 3TPXEfNjWDjdGBX7CVW+dla5cEilaUcne8IkCJLxWh9KEik3JHRRHGJouM2VcGfl96S8TihRzZvoroed6ti6WqEBmtzw3Wodatg+VyOeph4EYpr/1wXKtx8/wApIvJSwtmVi4MFU5aMqrSDE6ea73Mj2tcMyo5jMd6jmeWUHK8so/joWUoHOUgwuX4Po1QYz+3dszkDqMp4fklxBwXRsW10KXzPMTZ+sOPAveyxindmjkW8lGy+QsRlGPfZ+G6Z6h7mjem0Y+iWlkYcV4PIWL1iwBi8saCbGS5jN2p8M+X+Q7UNKEkROb3N6KOqkqm57TH2H3eDJAkSnh6/DNFu0Qg==',
                'Issuer organizational unit: No data available',
                'Issuer common name: DST Root CA X3',
                'ssuer organization: Digital Signature Trust Co.',
                'Extensions',
                'Authority key ID: c4a7b1a47b2c71fadbe14b9075ffc41560858910',
                'Certificate policies cps: http://cps.root-x1.letsencrypt.org',
                'Certificate policies ID: 2.23.140.1.2.1,1.3.6.1.4.1.44947.1.1.1',
                'Authority info access ocsp urls: http://isrg.trustid.ocsp.identrust.com',
                'Authority info access issuer urls: http://apps.identrust.com/roots/dstrootcax3.p7c',
                'Client auth: No data available',
                'Server auth: No data available',
                'DNS names: No data available',
                'IS CA: true',
                'CRL distribution points: http://crl.identrust.com/DSTROOTCAX3CRL.crl',
                'Key usage key encipherment: No data available',
                'Key usage value: 97',
                'Key usage is digital signature:',
                'Subject key ID: a84a6a63047dddbae6d139b7a64565eff3a8eca1']]
        self.set_font('Times','',12.0) 
        self.ln(0.5)
        th2 = pdf.font_size
        for row in data2:
            top = pdf.y
            for datum in row:
                self.multi_cell(epw, 1.6*th, str(datum),0,0,'L')
            self.ln(2*th2)





    
    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')
        self.rect(7, 7, 196, 283)
        self.rect(5, 5, 200, 287)
        



pdf = PDF()
pdf.alias_nb_pages()
pdf.add_page()
pdf.chapter()
pdf.set_font('Times', '', 12)
pdf.output('report_host_info.pdf', 'F')