from rest_framework import serializers
from app.models import Purpose

class PurposeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purpose
        fields = ['name', 'image']