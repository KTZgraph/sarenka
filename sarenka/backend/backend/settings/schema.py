import graphene
import api_cheat_sheet.schema


class Query(api_cheat_sheet.schema.Query, graphene.ObjectType): #dodawac jako arg z innych apek
    pass

schema = graphene.Schema(query=Query)