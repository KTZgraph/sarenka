import graphene
from graphene_django.types import DjangoObjectType
from .models import CWEModel


class CWEModelType(DjangoObjectType): # podobnie do serializer
    class Meta:
        model = CWEModel


class Query(graphene.ObjectType):
    all_cwe = graphene.List(CWEModelType)

    def resolve_all_cwe(self, info, **kwargs): # dodatkowe argumenty na pozniej
        return CWEModel.objects.all()
