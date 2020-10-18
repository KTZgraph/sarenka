from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response

from api_dns.a_record import ARecord, ARecordWrongFQDNError
from api_dns.serializers import ARecordDict, ARecordSerializer
from common.contact import Contact


class ARecordView(APIView):

    def get(self, request, fqdn='renmich.faculty.wmi.amu.edu.pl'):
        """
        Gets DNS A Record Data

        :param request: django request object
        :param fqdn: fully qualified domain name
        :return: dns data
        :example: fqdn='renmich.faculty.wmi.amu.edu.pl'
        """
        dns_func = {
            'ip': ARecord.get_ip,
            'cname': ARecord.get_cname,
            'mx': ARecord.get_mx,
            'ns': ARecord.get_ns,
            'dname': ARecord.get_dname,
            'aname': ARecord.get_aname
        }

        dns_data = {}
        for record_name in dns_func.keys():
            try:
                dns_data.update({record_name : dns_func.get(record_name)(fqdn)})
            except ARecordWrongFQDNError as err:
                dns_data.update({record_name: str(err)})
            except NotImplementedError:
                dns_data.update({record_name: Contact.get_contact(record_name.upper() + ' Record')})
            except KeyError:
                dns_data.update({"ARecord": f"record '{record_name}' is not supported"})

        obj = ARecordDict(dns_data)
        return Response(ARecordSerializer(obj).data)


class CrtShView(APIView):
    service = "https://crt.sh"
    repository = "https://github.com/crtsh/certwatch_db"

    def get(self, identity):
        """
        Identity (Domain Name, Organization Name, etc),
        a Certificate Fingerprint (SHA-1 or SHA-256) or a crt.sh ID:
        """
        url = f"{CrtShView.service}/?q={identity}"
        # https://crt.sh/?q=google.pl
        return JsonResponse({"CrtSh" : "Returns data from crt_sh_s"})
