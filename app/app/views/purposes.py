from rest_framework import viewsets, mixins
from rest_framework.response import Response
from app.models import Purpose
from app.serializers import PurposeSerializer

class PurposeViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Purpose.objects.all()
    serializer_class = PurposeSerializer
