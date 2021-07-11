from rest_framework import viewsets, mixins
from rest_framework.response import Response
from app.models import Color
from app.serializers import ColorSerializer

class ColorViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer
