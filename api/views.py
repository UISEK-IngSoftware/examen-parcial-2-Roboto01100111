from rest_framework import viewsets
from movies.models import Gore
from .serializers import GoreSerializer

class GoreViewSet(viewsets.ModelViewSet):
    queryset = Gore.objects.all()
    serializer_class = GoreSerializer
