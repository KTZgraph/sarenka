# from django.http import JsonResponse
# from rest_framework.views import APIView
# from rest_framework.response import Response

from bs4 import BeautifulSoup
import requests


# class CWETop25(APIView):
#
#     def get(self, request):
#         """
#         Zwraca informacje o TOP 25 najgroźniejszych słabościach oprogramowania
#         """
#         return JsonResponse({"response":"TOP 25 CWE"})


class CWEScrapper:
    top_25_url = "https://cwe.mitre.org/top25/archive/2020/2020_cwe_top25.html"

    def get_top_25(self):
        """
        SCRAPER - Pobiera dane ze strony
        :return:
        """
        source = requests.get(self.top_25_url).text
        soup = BeautifulSoup(source, 'lxml')
        # pobranie tabelki ze szczególami top 25 cwe
        detail_table = soup.find("table", {"id": "Detail"})

        # wszystkie wiersze tabeli
        rows = detail_table.findAll("tr")
        for r in rows[1:]:
            # bez pierwszego, bo pierwszy wiersz nie zawiera danych
            row_td = r.findAll("td")
            description= row_td[2].string
            score = row_td[3].string
            rank = r.b.string[1:-1]

            href = r.find("a")
            definition_url = href["href"]
            cwe_ID = href.string

            print(rank, description, score, definition_url, cwe_ID)




if __name__ == "__main__":
    cwe_scrapper = CWEScrapper()
    cwe_scrapper.get_top_25()
