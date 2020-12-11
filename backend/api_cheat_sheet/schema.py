import graphene
from graphene_django.types import DjangoObjectType
from .models import CWEModel


class CWEModelType(DjangoObjectType): # podobnie do serializer
    class Meta:
        model = CWEModel


class Query(graphene.ObjectType):
    all_cwe = graphene.List(CWEModelType)
    cwe = graphene.Field(CWEModelType,
                         id=graphene.Int(),
                         rank=graphene.Int(),
                         top_25=graphene.Boolean(),
                         code=graphene.Int()
                         )


    def resolve_all_cwe(self, info, **kwargs): # dodatkowe argumenty na pozniej
        return CWEModel.objects.all()

    def resolve_cwe(self, info, **kwargs): # dodatkowe argumenty na pozniej
        cwe_id = kwargs.get('id')
        cwe_rank = kwargs.get('rank')
        cwe_top_25 = kwargs.get('top_25')
        code = kwargs.get('code')

        if cwe_id is not None:
            cwe = CWEModel.objects.filter(pk=cwe_id)
            return cwe if cwe else None

        if cwe_rank is not None:
            cwe = CWEModel.objects.filter(cwe_rank=cwe_rank)
            return cwe if cwe else None

        if cwe_top_25 is not None:
            cwe = CWEModel.objects.filter(cwe_top_25=cwe_top_25)
            return cwe if cwe else None

        if code is not None:
            cwe = CWEModel.objects.filter(code=code)
            return cwe if cwe else None

        return None