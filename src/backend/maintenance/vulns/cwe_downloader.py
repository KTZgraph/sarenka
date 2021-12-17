from requests import get
from zipfile import ZipFile
from os import remove
from pathlib import Path

class CWEDownloader:
    _remote_url = 'https://cwe.mitre.org/data/xml/cwec_latest.xml.zip'
    _local_zip = 'cwe_list.xml.zip'

    def __init__(self):
        CWEDownloader.download()
        self.filepath = CWEDownloader.unzip()

    @staticmethod
    def download():
        data = get(CWEDownloader._remote_url)
        with open(CWEDownloader._local_zip, 'wb') as file:
            file.write(data.content)

    @staticmethod
    def unzip():
        dir_path = Path(__file__).parent.absolute()
        with ZipFile(CWEDownloader._local_zip, 'r') as zip_ref:
            extracted_file_name = zip_ref.namelist()
            zip_ref.extractall(dir_path)
        remove(CWEDownloader._local_zip)
        return extracted_file_name[0] # tylko jeden plik w zipie


if __name__ == "__main__":
    print(CWEDownloader().filepath)