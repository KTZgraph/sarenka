from .cve_circl_details import CveCirclDetailsError
from .cve_circl_connector import CveCirclConnector


class CveCirlVendorListError(Exception):
    """
    Zgłoszenie wyjąktu gdy nie można pobrac danych o dostawcy oprogramowania z serwisu https://cve.circl.lu"".
    """
    def __init__(self, message=None, errors=None):
        super().__init__(message)
        self.errors = errors


class CveCirlVendorList:
    """KLasa zwrcająca listę dostawców oprogramowania z serwisu https://cve.circl.lu"""
    def __init__(self, service_details):
        self.service_details = service_details

    def get_data(self):
        try:
            cve_cirl_details = self.service_details.cve_circl
            connector = CveCirclConnector(cve_cirl_details)
            response = connector.get_vendors_list()
            return response
        except CveCirclDetailsError as ex:
            raise CveCirlVendorListError("Invalid details for service https://cve.circl.lu.")
