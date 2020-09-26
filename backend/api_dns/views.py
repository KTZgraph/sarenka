from django.http import JsonResponse
from rest_framework.views import APIView
from api_dns.a_record import ARecord, ARecordWrongFQDNError
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

        response = []
        for record_name in dns_func.keys():
            try:
                response.append(dns_func.get(record_name)(fqdn))
            except ARecordWrongFQDNError as err:
                response.append({record_name: str(err)})
            except NotImplementedError:
                response.append(Contact.get_contact(record_name.upper() + ' Record'))
            except KeyError:
                response.append({"ARecord": f"record '{record_name}' is not supported"})

        return JsonResponse({"DNS": response})
