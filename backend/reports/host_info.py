from fpdf import FPDF, HTMLMixin

class PDF(FPDF, HTMLMixin):
    def header(self):
        self.set_font('Arial', 'B', 15)
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
        self.set_font('Times','B',14.0) 
        self.set_font('Times','',10.0) 
        self.ln(0.5)
        th = pdf.font_size

        for row in data:
            top = pdf.y
            for datum in row:
                offset = pdf.x + col_width
                self.multi_cell(col_width, 2*th, str(datum),0,0,'L')
            self.ln(2*th)



        data2 = [['Latitude: 52.2394',
                'Timezone: Europe/Warsaw',
                'Continent: Europe',
                'Registered country: Poland,',
                'Description: SPRINT-SDC',
                'RIR: unknown',
                'Routed prefix: 46.29.16.0/21']]
        self.set_font('Times','B',14.0) 
        self.set_font('Times','',10.0) 
        self.ln(0.5)
        th2 = pdf.font_size
       
        for row in data2:
            pdf.y = top
            for datum in row:
                pdf.x = offset               
                self.multi_cell(col_width,  2*th2, str(datum),0,0,'L')
            self.ln(2*th2)




        data2 = [['Path: 7018,3257,197226',
                'ASN: 197226',
                'Name: SPRINT-SDC',
                'DNS names: No data available',
                'DNS errors: No data available',
                'OS: No data available',
                'Updated at: 2020-10-11T04:32:48+00:00']]
        self.set_font('Times','B',14.0) 
        self.set_font('Times','',10.0) 
        self.ln(0.5)
        th2 = pdf.font_size
       
        for row in data2:
            pdf.y = top

            for datum in row:
                pdf.x = offset+col_width               

                self.multi_cell(col_width,  2*th2, str(datum),0,0,'L')
            self.ln(2*th2)







        self.ln(60)







        
        data = [['Web page title: HostingHouse.pl',
                'Web page body SHA256: b9b93998fa0c1b1f3c5da8469bb04254df54cd01060c8e035cfde18ecf1c1181',
                'Status code: 200',
                'Metadata',
                'Product: httpd',
                'Version: No data available',
                'Description: Apache httpd',
                'Manufacturer: Apache']]
        self.set_font('Times','B',14.0) 
        self.set_font('Times','',10.0) 
        self.ln(0.5)
        th = pdf.font_size

        for row in data:
            top = pdf.y
            for datum in row:
                offset = pdf.x + col_width
                self.multi_cell(col_width, 2*th, str(datum),0,0,'L')
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
        self.set_font('Times','B',14.0) 
        self.set_font('Times','',10.0) 
        self.ln(0.5)
        th2 = pdf.font_size
       
        for row in data2:
            pdf.y = top
            for datum in row:
                pdf.x = offset               
                self.multi_cell(col_width,  2*th2, str(datum),0,0,'L')
            self.ln(2*th2)




        data2 = [['Generator value: No data available',
                'DHE support: true',
                'Heartbleed: true',
                'Logjam attack: false',
                'Freak attack: false',
                'Poodle attack: No data available']]
        self.set_font('Times','B',14.0) 
        self.set_font('Times','',10.0) 
        self.ln(0.5)
        th2 = pdf.font_size
       
        for row in data2:
            pdf.y = top

            for datum in row:
                pdf.x = offset+col_width               

                self.multi_cell(col_width,  2*th2, str(datum),0,0,'L')
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
pdf.set_font('Times', '', 12)
pdf.output('report_host_info.pdf', 'F')