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
import pprint

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

    def __init__(self, host_address, id_cwe:str):
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



class NISTCVEScraper:
    """
    Dodatkowe źródło danych o podatnosciach CVE
    """
    nist_url = "https://nvd.nist.gov/vuln/detail/"
    # https://nvd.nist.gov/vuln-metrics/cvss/v2-calculator?vector=(AV:N/AC:M/Au:N/C:P/I:P/A:P)
    nist_vector_v2_url = "https://nvd.nist.gov/vuln-metrics/cvss/v2-calculator?vector="

    #https://www.first.org/cvss/calculator/3.0#CVSS:3.0/AV:A/AC:H/PR:H/UI:R/S:C/C:H/I:H/A:H
    nist_vector_v3_url = "https://www.first.org/cvss/calculator/3.0#CVSS:3.0/"

    # https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:A/AC:H/PR:L/UI:R/S:C/C:H/I:H/A:H
    nist_vector_v3_1_url = "https://www.first.org/cvss/calculator/3.1#"

    def __init__(self, id_cve, host_address= "NA SZTYWNO 127.0.0.1:8000"):
        self.id_cve = id_cve
        self.cve_url = self.nist_url + id_cve
        self.host_address = host_address

    def get_description(self, soup):
        description = soup.find("p", {"data-testid" : "vuln-description"})
        return description.text

    def get_base_score_v3(self, soup):
        base_score = soup.find("a", {"id" : "Cvss3NistCalculatorAnchor"})
        if base_score:
            return base_score.text

    def get_base_score_v2(self, soup):
        base_score = soup.find("a", {"id" : "Cvss2CalculatorAnchor"})
        if base_score:
            return base_score.text



    def get_vector_calculator_url(self, vector:str):
        # TODO: sprawdzic dla podatnosci w wersji 2.0 i 3.0
        """Common Vulnerability Scoring System Version
        Zwraca link do kalkulator vectora ataku na podstawie jego wersji.
        Brak spójności - stare podatnosci mają tylko wersje 2.0 lub 2.0 i 3.0
        najnowsze tylko 3.1 - ciągle sie to zmienia"""
        if vector.startswith("CVSS:3.1"):
            return self.nist_vector_v3_1_url + vector
        if vector.startswith("CVSS:3.0"):
            return self.nist_vector_v3_url + vector
        if vector.startswith("(") and vector.endswith(")"):
            return f"{self.nist_vector_v2_url}{vector}"
        return f"No Common Vulnerability Scoring System Version for CVE={self.id_cve}"

    def get_cvss3_vector(self, soup):
        """Zwraca Common Vulnerability Scoring System Version 3.0."""
        cvss3 = soup.find("span", {"class" : "tooltipCvss3NistMetrics"})
        if cvss3:
            cvss3 = cvss3.text
        else:
            cvss3 = ""
        return {
            "cvss3" : cvss3,
            "cvss3_url" : self.get_vector_calculator_url(cvss3)
        }

    def get_cvss2_vector(self, soup):
        """Zwraca Common Vulnerability Scoring System Version 2.0."""
        cvss2 = soup.find("span", {"data-testid" : "vuln-cvss2-panel-vector"})

        if cvss2:
            cvss2 = cvss2.text
        else:
            cvss2 = ""
        return {
            "cvss2" : cvss2,
            "cvss2_url" : self.get_vector_calculator_url(cvss2)
        }

    def get_hyperlinks(self, soup):
        result = []
        table = soup.find("table", {"data-testid": "vuln-hyperlinks-table"})
        td_list = table.findAll("td")
        for td in td_list:
            if td.find("a"):
                result.append(td.find("a")["href"])

        return result

    def get_cwe(self, soup):
        result = []
        table = soup.find("table", {"data-testid": "vuln-CWEs-table"})
        td_list = table.findAll("td")
        for td in td_list:
            if td.find("a"):
                ID_CWE = td.find("a").text
                mitre_url = td.find("a")["href"]
                result.append({
                    "ID_CWE": ID_CWE,
                    "cwe_mitre_url" : mitre_url,
                    "cwe_title": CWEDataScraper(self.host_address, td.find("a").text).get_title(),
                    # "sarenka_cwe_url":  self.host_address + reverse('get_by_cwe', kwargs={"id_cwe": ID_CWE}),
                })

        return result

    def get_cpe(self, soup):
        """
        Common Platform Enumeration
        https://nvd.nist.gov/products/cpe
        https://nvd.nist.gov/products/cpe/search
        """
        result =[]
        main_div = soup.findAll("div", {"class": "vuln-change-history-container"})

        for div in main_div:
            pre = div.find("pre")
            if pre:
                if pre.text.startswith("OR"):
                    cpe = pre.text.split("OR")[1]
                    result.append(cpe.strip())

        main_div = soup.findAll("div", {"class": "vuln-change-history-container"})
        for div in main_div:
            table = div.find("table", {"data-testid": "vuln-change-history-table" })
            for pre in table.findAll("pre"):
                if "cpe:" in pre.text:
                    cpe_text = pre.text.split("OR")[-1].strip()
                    # na koncu zostawiaja syf samao cpe *cpe:2.3:
                    cpe_list =[cpe for cpe in  cpe_text.split() if len(cpe) > 9]
                    result.extend(cpe_list)

        return result

    def get_published_date(self, soup):
        """Data publikacji publiczenj podatnosci."""
        published = soup.find("span", {"data-testid": "vuln-published-on"})
        return published.text

    def get_last_modified(self, soup):
        modified = soup.find("span", {"data-testid": "vuln-last-modified-on"})
        return modified.text

    def get_vuln_source(self, soup):
        modified = soup.find("span", {"data-testid": "vuln-current-description-source"})
        return modified.text

    def get_data(self):
        source = requests.get(self.cve_url).text
        soup = BeautifulSoup(source, 'lxml')

        return {
            "cve": self.id_cve,
            "description": self.get_description(soup),
            "cvss3": self.get_cvss3_vector(soup),
            "cvss2": self.get_cvss2_vector(soup),
            "base_score_v3": self.get_base_score_v3(soup),
            "base_score_v2": self.get_base_score_v2(soup),
            "hyperlinks": self.get_hyperlinks(soup),
            "cwe": self.get_cwe(soup),
            "cpe": self.get_cpe(soup),
            "published_date" : self.get_published_date(soup),
            "modified_date" : self.get_last_modified(soup),
            "vulnerability_source" : self.get_vuln_source(soup)
        }


if __name__ == "__main__":
    # nist_cve_scraper = NISTCVEScraper("CVE-2019-4570")
    # nist_cve_scraper = NISTCVEScraper("CVE-2014-8958")
    nist_cve_scraper = NISTCVEScraper("CVE-2009-1532")
    pprint.pprint(nist_cve_scraper.get_data())
    # nist_cve_scraper.get_data()
