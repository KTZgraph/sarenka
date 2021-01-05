from .models import CWEModel, TechnicalImpactModel, CausedByModel
from .cve_and_cwe.mitre_cwe_scrapers import CWEDataScraper


class CWECRUD:
    """
    Klasa odpowiedzialna za operacje bazodanow.
    Jesj zadaniem jest dodanie obiektu CWE do odpowiedniej bazy danych
    """

    def __init__(self, cwe_data):
        self.__cwe_data = cwe_data
        self.__cwe_id = self.get_cwe_id()

    @property
    def cwe_data(self):
        return self.__cwe_data

    @property
    def cwe_id(self):
        return self.__cwe_id

    @property
    def db_name(self):
        return self.get_database_name()

    def get_cwe_id(self):
        return self.cwe_data.get("ID_CWE", None)

    def get_database_name(self):
        """Wybiera odpowiednią nazwę bazy danych"""
        if self.cwe_id:
            # nazwy baz dancyh to CWE_NONE CWE_79
            return self.cwe_id.replace("-", "_").upper()

        return "CWE_NONE"  # jawnie ma mi zwrócić, że nie ma  cwe_id

    def __add_cwe_none_obj(self):
        print("no cwe id")
        cwe_db_obj, is_created = CWEModel.objects.using(self.db_name).get_or_create(
            cwe_id="None",
            title="None",
            description="None",
            likehood="None"
        )

        # jeśli obiekt ZOSTAL WLASNIE stworzony
        # created jest False jak już istnieje w bazie dancyh obiekt
        if is_created:
            TechnicalImpactModel.objects.using(self.db_name).create(
                title="None",
                cwe=cwe_db_obj
            )

            CausedByModel.objects.using(self.db_name).create(
                field="None",
                process="None",
                description="None",
                cwe=cwe_db_obj
            )

    def add(self):
        """"
        Dodaje obiekt CWE do odpowiedniej bazy danych.
        """
        if self.db_name == "CWE_NONE":
            # nietypowa pojedyncza sytuakcja
            self.__add_cwe_none_obj()
            return

        # gdy normalnie CWE obiekt ma id
        print("TUUUUUUUUUUUUUUUUUUU")
        print("self.db_name: ", self.db_name)
        cwe_data_scraper = CWEDataScraper(self.cwe_id).get_data()

        cwe_db_obj, is_created = CWEModel.objects.using(self.db_name).get_or_create(
            cwe_id=cwe_data_scraper["ID_CWE"],
            title=cwe_data_scraper["title"],
            description=cwe_data_scraper["description"],
            likehood=cwe_data_scraper["likehood"]
        )

        # jeśli obiekt ZOSTAL WLASNIE stworzony
        # created jest False jak już istnieje w bazie dancyh obiekt
        if is_created:
            for technical_impact in cwe_data_scraper["technical_impact"]:
                TechnicalImpactModel.objects.using(self.db_name).create(
                    title=technical_impact,
                    cwe=cwe_db_obj
                )

            # for caused_by in cwe_data_scraper["caused_by"]:
            caused_by = cwe_data_scraper["caused_by"]
            CausedByModel.objects.using(self.db_name).create(
                field=caused_by["field"],
                process=caused_by["process"],
                description=caused_by["description"],
                cwe=cwe_db_obj
            )

    def __get_dict(self, cwe_db_obj):
        # tODO: tymczasowe rozwiazanie -> serializery
        response = {}
        response.update({"cwe_id": cwe_db_obj.cwe_id})
        response.update({"title": cwe_db_obj.title})
        response.update({"description": cwe_db_obj.description})
        response.update({"likehood": cwe_db_obj.likehood})

        cwe_technical_model = []
        for i in cwe_db_obj.cwe_technical_model.all():
            cwe_technical_model.append({"title": i.title})

        response.update({"cwe_technical_model": cwe_technical_model})

        cwe_caused_by = []
        for i in cwe_db_obj.cwe_caused_by.all():
            cwe_caused_by.append({"field": i.field})
            cwe_caused_by.append({"process": i.process})
            cwe_caused_by.append({"description": i.description})

        response.update({"cwe_caused_by": cwe_caused_by})

        return response

    def get(self):
        # pwoinien byc jeden taki obiekt w bazie konkretnej
        cwe_db_obj = CWEModel.objects.using(self.db_name).first()
        return self.__get_dict(cwe_db_obj) #TODO tyczasowe rozwiązanie

