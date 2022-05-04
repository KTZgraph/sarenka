""" 
pip install django-extensions
settings.py dopisać INSTALLED_APPS =[ ..., 'django-extensions', ...]
stworzyć folder srcripts a w nim scripts/__init__.py pusty

załadowanie danych:
python manage.py runscript cve_list_load # BEZ ROZSZRZERZENIA PY
"""
from re import S
import stat
from bs4 import BeautifulSoup
from requests import get
from pathlib import Path
from zipfile import ZipFile
from os import remove
import json


from apps.vulnerabilities.models import CVE


DIR_PATH = Path(__file__).parent.absolute()
MAIN_URL = "https://nvd.nist.gov"  # bez / na końcu

FEEDER_URL = "https://nvd.nist.gov/vuln/data-feeds#JSON_FEED"


class CVEDownloader:
    def __init__(self) -> None:
        files_urls = self.scrap()
        zip_filenames = self.download(files_urls)
        self.json_filenames = self.unzip(zip_filenames)

    @staticmethod
    def scrap() -> list:
        files_urls = []
        source = get(FEEDER_URL).text
        soup = BeautifulSoup(source, "lxml")

        # <div id="divJSONFeeds" class="row">
        soup = soup.find("div", {"id": "divJSONFeeds"})
        # <table class="xml-feed-table table table-striped table-condensed">
        soup = soup.find("table")  # tylko jedna tabela w sordku diva

        for a in soup.find_all("a", href=True):
            href = a["href"]
            if href.split(".")[-1] == "zip":
                files_urls.append(MAIN_URL + href)

        return files_urls

    @staticmethod
    def download(files_urls: list) -> list:
        zip_filenames = []

        for file_url in files_urls:
            zip_filename = file_url.split("/")[-1]
            data = get(file_url)
            with open(DIR_PATH.joinpath(zip_filename), "wb") as f:
                f.write(data.content)
                zip_filenames.append(zip_filename)

        return zip_filenames

    @staticmethod
    def unzip(zip_filenames: list) -> list:
        json_filenames = []

        for zip_filename in zip_filenames:
            zip_filename = DIR_PATH.joinpath(zip_filename)

            with ZipFile(zip_filename, "r") as zip_ref:
                extracted_file_name = zip_ref.namelist()
                zip_ref.extractall(DIR_PATH)

            # usuwanie pobranych zipów
            remove(zip_filename)
            # tylko jeden plik w zipie
            json_filenames.append(extracted_file_name[0])

        return json_filenames


class CVEParsed:
    def __init__(
        self,
        cve_id: str,
        cwe_id: str,
        description: str,
        cpe_list: list,
        cvss_v3,
        cvss_v2,
        is_ac_insuf_info,
        is_obtain_all_privilege,
        is_obtain_user_privilege,
        is_user_interaction_required,
        published_date: str,
        last_modified_date: str,
    ) -> None:

        self.cve_id = cve_id
        self.cwe_id = cwe_id
        self.description = description

        self.cpe_list = cpe_list

        self.cvss_v2 = cvss_v2
        self.cvss_v3 = cvss_v3

        self.is_ac_insuf_info = is_ac_insuf_info
        self.is_obtain_all_privilege = is_obtain_all_privilege
        self.is_obtain_user_privilege = is_obtain_user_privilege
        self.is_user_interaction_required = is_user_interaction_required

        self.published = published_date
        self.updated = last_modified_date


class CVEFileParser:
    @staticmethod
    def parse(filename: str):
        # jeden plik
        filepath = str(DIR_PATH.joinpath(filename))

        with open(filepath, encoding="utf-8-sig") as f:
            data = json.load(f)

        # główny klucz całego pliku
        items = data["CVE_Items"]

        parsed_items = []
        # każde CVE z listy
        # for item in items[:1]:
        for item in items[184:186]:
            # pprint(CVEParser(item["cve"]))

            # klucze 2 stopnia
            cve = CVEParser(item["cve"])
            cpe_matches = ConfigurationsParser(item["configurations"])

            print(cve.id)
            for cpe in cpe_matches.cpe_matches:
                print(cpe.is_vulnerable)
                print(cpe.cpe_23_uri)
                print(cpe.version_start_including)
                print(cpe.version_end_excluding)

            impact = ImpactParser(item["impact"])
            print("_______________impact_______________")

            if impact.cvss_v3:
                print("______cvss_v___________")
                print(impact.cvss_v3.version)
                print(impact.cvss_v3.code)
                print(impact.cvss_v3.base_score)
                print(impact.cvss_v3.base_severity)
                print(impact.cvss_v3.exploitability_score)
                print(impact.cvss_v3.impact_score)

            if impact.cvss_v2:
                print("______cvss_v2___________")
                print(impact.cvss_v2.version)
                print(impact.cvss_v2.code)
                print(impact.cvss_v2.base_score)
                print(impact.cvss_v2.base_severity)
                print(impact.cvss_v2.exploitability_score)
                print(impact.cvss_v2.impact_score)

            print("_______________is impact_______________")
            print(impact.is_ac_insuf_info)
            print(impact.is_obtain_all_privilege)
            print(impact.is_obtain_user_privilege)
            print(impact.is_user_interaction_required)

            print("\n\n\n")

            cve_parsed = CVEParsed(
                # (2) klucz "cve"
                cve_id=cve.id,
                cwe_id=cve.cwe,
                description=cve.description,
                # (2) klucz "configurations" (3) klucz "nodes" lista
                cpe_list=cpe_matches.cpe_matches,
                cvss_v3=impact.cvss_v3,
                cvss_v2=impact.cvss_v2,
                is_ac_insuf_info=impact.is_ac_insuf_info,
                is_obtain_all_privilege=impact.is_obtain_all_privilege,
                is_obtain_user_privilege=impact.is_obtain_user_privilege,
                is_user_interaction_required=impact.is_user_interaction_required,
                published_date=item["publishedDate"],
                last_modified_date=item["lastModifiedDate"],
            )

            parsed_items.append(cve_parsed)

        return parsed_items


class CVEParser:
    def __init__(self, cve: dict) -> None:
        # drugi poziom klucza "cve:"
        self.cve = cve

        self.id = self.get_id()
        print(self.id)

        self.cwe = self.get_cwe()
        print(self.cwe)

        self.description = self.get_description()
        print(self.description)

    def get_id(self):
        return self.cve["CVE_data_meta"]["ID"]

    def get_cwe(self):
        # nie zawsze jest
        try:
            return self.cve["problemtype"]["problemtype_data"][0]["description"][0][
                "value"
            ]
        except IndexError:
            return None

    def get_description(self):
        try:
            return self.cve["description"]["description_data"][0]["value"]
        except IndexError:
            return None


class CPEMatch:
    def __init__(
        self,
        is_vulnerable: bool,
        cpe_23_uri: str,
        version_start_including: str,
        version_end_excluding: str,
    ) -> None:
        self.is_vulnerable = is_vulnerable
        self.cpe_23_uri = cpe_23_uri
        self.version_start_including = version_start_including
        self.version_end_excluding = version_end_excluding


class ConfigurationsParser:
    # drugi poziom klucza "configurations:"
    # np.: "CVE-2022-0847"
    def __init__(self, configurations: dict) -> None:
        self.configurations = configurations
        self.cpe_matches = self.get_cpe_matches()

    def get_cpe_matches(self):
        cpe_match_obj_list = []
        for node in self.configurations["nodes"]:
            # jednym nodzie jedno cmpe_match

            cpe_match_list = node["cpe_match"]
            for cpe_match_dict in cpe_match_list:
                cpe_match_obj_list.append(
                    CPEMatch(
                        is_vulnerable=cpe_match_dict.get("vulnerable"),
                        cpe_23_uri=cpe_match_dict.get("cpe23Uri"),
                        version_start_including=cpe_match_dict.get(
                            "versionStartIncluding"
                        ),
                        version_end_excluding=cpe_match_dict.get("versionEndExcluding"),
                    )
                )
        return cpe_match_obj_list


class Vector:
    def __init__(
        self,
        version,
        code,
        base_score,
        base_severity,
        exploitability_score,
        impact_score,
    ) -> None:

        self.version = version
        self.code = code
        self.base_score = base_score
        self.base_severity = base_severity
        self.exploitability_score = exploitability_score
        self.impact_score = impact_score


class ImpactParser:
    # drugi poziom klucza "impact:"
    def __init__(self, impact: dict) -> None:
        self.impact = impact
        # dane z baseMetricV3
        self.cvss_v3 = self.get_cvss_v3()

        # dane z baseMetricV2
        self.cvss_v2 = self.get_cvss_v2()

        self.is_ac_insuf_info = self.get_is_ac_insuf_info()
        self.is_obtain_all_privilege = self.get_is_obtain_all_privilege()
        self.is_obtain_user_privilege = self.get_is_obtain_user_privilege()
        self.is_user_interaction_required = self.get_is_user_interaction_required()

    def get_cvss_v3(self):
        try:
            return Vector(
                version=self.impact["baseMetricV3"]["cvssV3"]["version"],
                code=self.impact["baseMetricV3"]["cvssV3"]["vectorString"],
                base_score=self.impact["baseMetricV3"]["cvssV3"]["baseScore"],
                base_severity=self.impact["baseMetricV3"]["cvssV3"]["baseSeverity"],
                exploitability_score=self.impact["baseMetricV3"]["exploitabilityScore"],
                impact_score=self.impact["baseMetricV3"]["impactScore"],
            )
        except KeyError:
            # żeby sortować po tych co nie mają wektora
            return Vector(None, None, None, None, None, None)

    # dane z baseMetricV2
    def get_cvss_v2(self):
        try:
            return Vector(
                version=self.impact["baseMetricV2"]["cvssV2"]["version"],
                code=self.impact["baseMetricV2"]["cvssV2"]["vectorString"],
                base_score=self.impact["baseMetricV2"]["cvssV2"]["baseScore"],
                base_severity=self.impact["baseMetricV2"]["severity"],
                exploitability_score=self.impact["baseMetricV2"]["exploitabilityScore"],
                impact_score=self.impact["baseMetricV2"]["impactScore"],
            )
        except KeyError:
            # żeby sortować po tych co nie mają wektora
            return Vector(None, None, None, None, None, None)

    def get_is_ac_insuf_info(self):
        try:
            return self.impact["baseMetricV2"]["acInsufInfo"]
        except KeyError:
            return None

    def get_is_obtain_all_privilege(self):
        try:
            return self.impact["baseMetricV2"]["obtainAllPrivilege"]
        except KeyError:
            return None

    def get_is_obtain_user_privilege(self):
        try:
            return self.impact["baseMetricV2"]["obtainOtherPrivilege"]
        except KeyError:
            return None

    def get_is_user_interaction_required(self):
        try:
            return self.impact["baseMetricV2"]["userInteractionRequired"]
        except KeyError:
            return None


def run():
    # json_filenames = CVEDownloader().json_filenames
    # pprint(json_filenames)

    json_filenames = [
        "nvdcve-1.1-modified.json",
        "nvdcve-1.1-recent.json",
        "nvdcve-1.1-2022.json",
        "nvdcve-1.1-2021.json",
        "nvdcve-1.1-2020.json",
        "nvdcve-1.1-2019.json",
        "nvdcve-1.1-2018.json",
        "nvdcve-1.1-2017.json",
        "nvdcve-1.1-2016.json",
        "nvdcve-1.1-2015.json",
        "nvdcve-1.1-2014.json",
        "nvdcve-1.1-2013.json",
        "nvdcve-1.1-2012.json",
        "nvdcve-1.1-2011.json",
        "nvdcve-1.1-2010.json",
        "nvdcve-1.1-2009.json",
        "nvdcve-1.1-2008.json",
        "nvdcve-1.1-2007.json",
        "nvdcve-1.1-2006.json",
        "nvdcve-1.1-2005.json",
        "nvdcve-1.1-2004.json",
        "nvdcve-1.1-2003.json",
        "nvdcve-1.1-2002.json",
    ]

    CVE.objects.all().delete()

    for cve_file in [json_filenames[1]]:
        CVEFileParser.parse(cve_file)
