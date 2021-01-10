from fpdf import FPDF, HTMLMixin
import json
import requests

class PDFHardwareInfo(FPDF, HTMLMixin):


    def header(self):
        self.set_font('Arial', 'B', 16)


    def headerOnlyFirstSide(self):
        self.image('../../logo.png',90,15, 30)
        self.cell(0, 100, 'Information about your computer', 0, 0, 'C')
        self.ln(60)


    def chapter(self, link):
        #GET JSON
        response = requests.get(link)
        dataJson = json.loads(response.text)
        epw = self.w - 2*self.l_margin
        col_width = epw/2
        self.set_font('Times','',12.0)
        th = self.font_size



        #FIRST COLUMN - FITST TABLE - TITLE
        self.ln(10)
        self.set_font('Times','B',16.0) 
        top = self.y
        self.set_text_color(192,11,38)
        self.cell(col_width,self.font_size, 'BIOS', 0, 0, 'L')
        self.ln(10)
        self.set_text_color(0,0,0)
        self.set_font('Times','',12.0)



        #FIRST COLUMN - FITST TABLE - TEXT
        for key in dataJson["bios"]:
            self.multi_cell(col_width, 1.6*th, key+": "+dataJson["bios"][key],0,0,'L')                         
        offset = self.x + col_width
        self.ln(10)



        #FIRST COLUMN - FITST TABLE - TITLE
        self.set_font('Times','B',16.0) 
        self.set_text_color(192,11,38)
        self.cell(col_width,self.font_size, 'COMPUTER', 0, 0, 'L')
        self.ln(10)

        #FIRST COLUMN - FITST TABLE - TEXT
        self.set_font('Times','',12.0)   
        self.set_text_color(0, 0, 0)
        for key in dataJson["computer_information"]:
            self.multi_cell(col_width, 1.6*th, key.replace('_', ' ')+": "+dataJson["computer_information"][key],0,0,'L')                         
        offset = self.x + col_width


        #FIRST COLUMN - FITST TABLE - TITLE
        self.ln(10)
        self.set_font('Times','B',16.0) 
        self.set_text_color(192,11,38)
        self.cell(col_width,self.font_size, 'MOTHERBOARD', 0, 0, 'L')
        self.ln(10)



        #FIRST COLUMN - FITST TABLE - TEXT
        self.set_font('Times','',12.0)   
        self.set_text_color(0, 0, 0)
        for key in dataJson["motherboard_information"]:
            self.multi_cell(col_width, 1.6*th, key.replace('_', ' ')+": "+dataJson["motherboard_information"][key],0,0,'L')                         
        offset = self.x + col_width



        #SECOND COLUMN - FITST TABLE - TITLE
        self.y = top
        self.x = self.x +col_width
        self.set_font('Times','B',16.0) 
        self.set_text_color(192,11,38)
        self.cell(col_width,self.font_size, 'OPERATION SYSTEM', 0, 0, 'L')
        self.ln(10)



        #SECOND COLUMN - FITST TABLE - TEXT
        self.set_font('Times','',12.0)   
        self.set_text_color(0, 0, 0)
        for key in dataJson["operation_system"]:
            self.x = self.x +col_width
            self.multi_cell(col_width, 1.6*th, key.replace('_', ' ')+": "+dataJson["operation_system"][key],0,0,'L')   
        self.ln(10)


        #SECOND COLUMN - FITST TABLE - TITLE
        top = self.y
        self.x = self.x +col_width
        self.set_font('Times','B',16.0) 
        self.set_text_color(192,11,38)
        self.cell(col_width,self.font_size, 'HARD DRIVE ', 0, 0, 'L')
        self.ln(10)


        #SECOND COLUMN - FITST TABLE - TEXT
        self.set_text_color(0, 0, 0)
        for key in dataJson["hard_drive_info"]:
            self.x = self.x +col_width
            self.set_font('Times','B',14.0)   
            self.multi_cell(col_width, 1.6*th, key,0,0,'L')      
            for key2 in dataJson["hard_drive_info"][key]:
                self.x = self.x +col_width
                self.set_font('Times','',12.0)   
                self.multi_cell(col_width, 1.6*th, key2.replace('_', ' ')+": "+dataJson["hard_drive_info"][key][key2],0,0,'L')                           


    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.set_text_color(0,0,0)
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')
        self.rect(7, 7, 196, 283)
        self.rect(5, 5, 200, 287)
        