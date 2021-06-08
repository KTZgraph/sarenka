from rest_framework import generics


from .models import CensysCredentials, ShodanCredentials
from .serializers import CensysCredentialsSerializer, ShodanCredentialsSerializer


class CredentialsCensys(generics.UpdateAPIView):
    # queryset = CensysCredentials.objects.all()  # wszystkie posty nawet nie opublikowane
    # serializer_class = CensysCredentialsSerializer
    pass


class CredentialsShodan(generics.UpdateAPIView):
    # queryset = ShodanCredentials.objects.all() # wszystkie posty nawet nie opublikowane
    # serializer_class = ShodanCredentialsSerializer
    pass
