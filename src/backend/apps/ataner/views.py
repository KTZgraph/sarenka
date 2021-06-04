from rest_framework.response import Response
from rest_framework import mixins, generics
from .image_analyzer.text_extractor import TextExtractor


class AtanerAPI(generics.GenericAPIView, mixins.RetrieveModelMixin):

    def get(self, request):
        extractor = TextExtractor()
        result = extractor.extract_from_file()
        return Response({
            'text_extractor': result
        })
