import requests
from bs4 import BeautifulSoup

from backend.api_searcher.scrapers.mitre_cwe_scrapers import CWEDataScraper


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
    # print(nist_cve_scraper.get_data())
    # nist_cve_scraper.get_data()
