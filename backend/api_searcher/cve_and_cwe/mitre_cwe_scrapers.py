"""
Scrapery do danych ze strony https://cwe.mitre.org/

CVE-2019-4570
https://nvd.nist.gov/vuln/detail/CVE-2019-4570#vulnCurrentDescriptionTitle
Scrapery do danych ze strony https://nvd.nist.gov
"""
from rest_framework.reverse import reverse
from typing import List, Dict
from bs4 import BeautifulSoup
import requests
import re


class CWETableTop25Scraper:
    """
    Scraper danych - pobiera dane z tabeli dla top 25 słabości oprogramowania z https://cwe.mitre.org/top25/archive/2020/2020_cwe_top25.html.
    """
    top_25_url = "https://cwe.mitre.org/top25/archive/2020/2020_cwe_top25.html"
    cwe_mitre_url = "https://cwe.mitre.org"

    def __init__(self, host_address):
        self.host_address = host_address

    def get_top_25(self):
        """
        SCRAPER - Pobiera dane ze strony - zwraca top 25 najpopularniejszych słabości.
        :return:
        """
        result = []
        source = requests.get(CWETableTop25Scraper.top_25_url).text
        soup = BeautifulSoup(source, 'lxml')
        # pobranie tabelki ze szczególami top 25 cwe
        detail_table = soup.find("table", {"id": "Detail"})

        # wszystkie wiersze tabeli
        rows = detail_table.findAll("tr")
        for r in rows[1:]:
            # bez pierwszego, bo pierwszy wiersz nie zawiera danych
            row_td = r.findAll("td")
            description = row_td[2].string
            score = row_td[3].string
            rank = r.b.string[1:-1]

            href = r.find("a")
            definition_url = CWETableTop25Scraper.cwe_mitre_url + href["href"]
            ID_CWE = href.string

            result.append({
                "rank" : rank,
                "ID_CWE": ID_CWE,
                "description": description,
                "score": score,
                "definition_url" : definition_url,
                # adres do wnętrza apliakcji
                "sarenka_url": self.host_address + reverse('get_by_cwe', kwargs={"id_cwe": ID_CWE}),
            })

        return result


class CWEDataScraper:
    cwe_mitre_url = "https://cwe.mitre.org/data/definitions/"

    def __init__(self, id_cwe: str, host_address=None):
        self.host_address = host_address
        if "-" in id_cwe:
            id_cwe = id_cwe.split("-")[1] # dla postaci CWE-79
        self.id_cwe = id_cwe
        self.cwe_url = self.generate_definition_url()

        source = requests.get(self.cwe_url).text
        self.soup = BeautifulSoup(source, 'lxml')

    def generate_definition_url(self)->str:
        return self.cwe_mitre_url + self.id_cwe + ".html"

    def get_title(self):
        """Zwraca tytuł slabości."""
        try:
            title = self.soup.find("h2").string
            title = title.split(":")[1]
        except AttributeError:
            title = self.soup.find("h2")
        return title.strip()

    def get_description(self)->str:
        description = self.soup.find("div", {"id": "oc_" + self.id_cwe + "_Description" })
        return description.string

    def get_likelihood(self)->str:
        """Poziom prawdopodobieństwa istnienia exploitów i samej exploitacji słabości."""
        likehood = self.soup.find("div", {"id": "oc_"+ self.id_cwe + "_Likelihood_Of_Exploit" })
        return likehood.string

    def get_likelihood(self)->str:
        """Poziom prawdopodobieństwa istnienia exploitów i samej exploitacji słabości."""
        likehood = self.soup.find("div", {"id": "oc_"+ self.id_cwe + "_Likelihood_Of_Exploit" })
        if likehood:
            return likehood.string
        return "No information about exploitation likehood"

    def get_technical_impact(self)->List[str]:
        """Częsre konswekwencje exploitacji słabości."""
        result = []

        div = self.soup.find("div", {"id": "oc_" + self.id_cwe + "_Common_Consequences" })
        table = div.find("table")
        tr = table.findAll("tr")
        for i in tr[1:]: # be zpierwszego wiersza bo tam nie ma danych
            row = i.find("p", {"class": "smaller"})
            # tylko jeden wynik - re.findall zwraca listę
            impact = re.findall("<i>(.*?)</i>", str(row))[0]
            impact = impact.split(";")
            impact = [i.strip() for i in impact]
            result.extend(impact)

        # bez duplikatow - wydajniej zamienic na slwonik
        return list(set(result))

    def get_caused_by(self):
        """
        Etap podczas którego powstaje podatność. Np. podczas implementacji.
        """
        div_main = self.soup.find("div", {"id": "oc_" + self.id_cwe +"_Modes_Of_Introduction"})
        table = div_main.find("table")
        tr = table.findAll("tr")

        field = tr[1].text # np.: Architecture and Design
        all_td = tr[-1].findAll("td")

        process = all_td[0].text # np.: Implementation
        description = all_td[1].text # This weakness is caused during implementation of an architectural security tactic.
        description = description.split(":")[-1].strip()

        return {
            "field": field,
            "process": process,
            "description": description
        }

    def get_cve_examples(self)->List[Dict]:
        """
        Przykładowe podatności bezpieczeństwa w konkretnych oprogramowanaich dla tego typu słabości oprogramowania.
        """
        result = []
        div_main = self.soup.find("div", {"id": "oc_" + self.id_cwe +"_Observed_Examples"})
        table = div_main.find("table", {"class": "Detail"})
        tr_list = table.findAll("tr")

        for tr in tr_list[1:]: # w pierwszym wierszu nie ma danych
            id_CVE = None
            description = None

            if tr.find("div", {"class": "indent"}):
                description = tr.find("div", {"class": "indent"}).text

            if tr.find("a"):
                id_CVE = tr.find("a").text
                mitre_url = tr.find("a")["href"]

            result.append({
                "id_CVE": id_CVE,
                "description": description,
                "mitre_url": mitre_url, # https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2006-3568
                "sarenka_url": self.host_address + reverse('get_by_cve', kwargs={"code": id_CVE}),
            })

        return result

    def get_data(self)->Dict:
        """
        Zwraca wszystkie dane wyciągniete podczas scrapowania.
        """
        source = requests.get(self.cwe_url).text
        soup = BeautifulSoup(source, 'lxml')

        result= {
            "ID_CWE" : "CWE-"+self.id_cwe,
            "title": self.get_title(),
            "description": self.get_description(),
            "likehood": self.get_likelihood(),
            "technical_impact": self.get_technical_impact(),
            "caused_by": self.get_caused_by(),
            "cve_examples": self.get_cve_examples()
        }

        return result

