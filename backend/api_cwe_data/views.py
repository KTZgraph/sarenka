# from rest_framework.views import APIView
# from rest_framework.response import Response

from bs4 import BeautifulSoup
import requests
import re
from collections import namedtuple


# class CWETop25(APIView):
#     def get(self, request):
#         """
#         Widok - zwraca informacje o TOP 25 najgroźniejszych słabościach oprogramowania
#         """
#         return Response({"response": CWETableTop25Scraper.get_top_25()})
#
#
# class CWETableTop25Scraper:
#     """
#     Scraper danych - pobiera dane z tabeli dla top 25 słabości oprogramowania z https://cwe.mitre.org/top25/archive/2020/2020_cwe_top25.html.
#     """
#     top_25_url = "https://cwe.mitre.org/top25/archive/2020/2020_cwe_top25.html"
#     cwe_mitre_url = "https://cwe.mitre.org"
#
#     @staticmethod
#     def get_top_25():
#         """
#         SCRAPER - Pobiera dane ze strony
#         :return:
#         """
#         result = []
#         CWE = namedtuple("CWE", 'rank cwe_ID description score definition_url')
#
#         source = requests.get(CWETableTop25Scraper.top_25_url).text
#         soup = BeautifulSoup(source, 'lxml')
#         # pobranie tabelki ze szczególami top 25 cwe
#         detail_table = soup.find("table", {"id": "Detail"})
#
#         # wszystkie wiersze tabeli
#         rows = detail_table.findAll("tr")
#         for r in rows[1:]:
#             # bez pierwszego, bo pierwszy wiersz nie zawiera danych
#             row_td = r.findAll("td")
#             description = row_td[2].string
#             score = row_td[3].string
#             rank = r.b.string[1:-1]
#
#             href = r.find("a")
#             definition_url = CWETableTop25Scraper.cwe_mitre_url + href["href"]
#             cwe_ID = href.string
#
#             result.append(CWE(
#                 rank,
#                 cwe_ID,
#                 description,
#                 score,
#                 definition_url
#             ))
#
#         return result
#
#
# class CWEData(APIView):
#     """
#     Zwraca infromacje o Common Weakness Enumeration na podstawie podane numeru CWE ID.
#     http://127.0.0.1:8000/cwe/79
#     http://127.0.0.1:8000/cwe/CWE-79
#     http://127.0.0.1:8000/cwe/cwe-79
#
#     """
#     cwe_mitre_url = "https://cwe.mitre.org/data/definitions/"
#
#     def get(self, request, id_cwe="79"):
#         """
#
#         :param request:
#         :param id_cwe: string będący ID CWE w postaci 79 lub CWE-79
#         :return:
#         """
#         if "-" in id_cwe:
#             id_cwe = id_cwe.split("-")[1] # dla postaci CWE-79
#
#         def_url = self.cwe_mitre_url + id_cwe + ".html"
#         print(def_url)
#
#         return Response({"response:", def_url})


class CWEDataScraper:
    cwe_mitre_url = "https://cwe.mitre.org/data/definitions/"

    def __init__(self, id_cwe):
        if "-" in id_cwe:
            id_cwe = id_cwe.split("-")[1] # dla postaci CWE-79
        self.id_cwe = id_cwe
        self.definition_url = self.generate_definition_url()

    def generate_definition_url(self):
        return self.cwe_mitre_url + self.id_cwe + ".html"

    def get_title(self, soup):
        return soup.findAll("h2")

    def get_description(self, soup):
        description = soup.find("div", {"id": "oc_" + self.id_cwe + "_Description" })
        return description.string

    def get_likelihood(self, soup):
        """Poziom prawdopodobieństwa istnienia exploitów i samej exploitacji słabości."""
        likehood = soup.find("div", {"id":"oc_"+ self.id_cwe + "_Likelihood_Of_Exploit" })
        return likehood.string

    def get_technical_impact(self, soup):
        """Częsre konswekwencje exploitacji słabości."""
        result = []

        div = soup.find("div", {"id":"oc_"+ self.id_cwe + "_Common_Consequences" })
        table = div.find("table")
        tr = table.findAll("tr")
        for i in tr[1:]: # be zpierwszego wiersza bo tam nie ma danych
            row = i.find("p", {"class": "smaller"})
            # tylko jeden wynik - re.findall zwraca listę
            impact = re.findall("<i>(.*?)</i>", str(row))[0]
            result.append(impact.strip())

        return result

    def get_data(self):
        source = requests.get(self.definition_url).text
        soup = BeautifulSoup(source, 'lxml')
        title = self.get_title(soup)
        description = self.get_description(soup)
        likehood = self.get_likelihood(soup)
        technical_impact = self.get_technical_impact(soup)

        return technical_impact


if __name__ == "__main__":
    cwe_data_scraper = CWEDataScraper("79")
    # print(cwe_data_scraper.generate_definition_url())
    print(cwe_data_scraper.get_data())
