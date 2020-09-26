from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response

from api_dns.a_record import ARecord, ARecordWrongFQDNError
from api_dns.serializers import ARecordDict, ARecordSerializer
from common.contact import Contact


class ARecordAPIView(APIView):

    def get(self, request, fqdn):
        """
        DNS A Record Data
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
