"""
Moduł będzie wymgać pracy maintenace
"""
import requests
import PyPDF2
import re


class CWEAllFileParser:
    """Parsuje wsyzstkie kody CWE z pliku pdf https://cwe.mitre.org/data/published/cwe_latest.pdf
    tak, żeby zapisac, je do bazy danych a potem dodac im relacje z kodów CWE"""

    cwe_latest_file_url = "https://cwe.mitre.org/data/published/cwe_latest.pdf"
    CHUNK_SIZE = 8096
    NUMBER_OF_PAGES = 26 # nadmiarowa ilosc stron na których znajdują się kody CWE


    def __init__(self):
        self.__local_file_path = "cwe_latest.pdf"
        self.__download_pdf()
        self.__pdf_file_obj = self.__get_pdf_file_obj()
        self.__creation_date = self.__pdf_file_obj.documentInfo["/CreationDate"]
        self.__cwes_set = self.__get_all_cwes()

    @property
    def creation_date(self):
        return self.__creation_date

    @property
    def cwes(self):
        return self.__cwes_set

    def __download_pdf(self):
        response = requests.get(self.cwe_latest_file_url, stream=True)

        with open(self.__local_file_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=self.CHUNK_SIZE):
                f.write(chunk)

    def __get_pdf_file_obj(self):
        pdf_file_obj = open(self.__local_file_path, "rb")
        pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj)
        return pdf_reader

    def __get_all_cwes(self):
        """Skraca plik do pierwszych 25 stron w który sa wszystkie CWE kody
        Rzowiązuje problem zbyt dużego pliku po parsowania w bibliotece pdfminer"""

        cwe_list = []
        regex = re.compile("CWE-\d+")

        for i in range(self.NUMBER_OF_PAGES):
            page_obj = self.__pdf_file_obj.getPage(i)
            page_str = page_obj.extractText()
            cwe_list.extend(regex.findall(page_str))

        return set(cwe_list)


if __name__ == "__main__":
    parser = CWEAllFileParser()
    # parser.download_pdf()
    print(parser.cwes)

