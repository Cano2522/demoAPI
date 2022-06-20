from rest_framework import serializers
from OMNICLAS34.models import *

class OMC34Nivel1Serializer(serializers.ModelSerializer):
    class Meta:
        model = OMC34Nivel1
        fields = '__all__'

class OMC34Nivel2Serializer(serializers.ModelSerializer):
    class Meta:
        model = OMC34Nivel2
        fields = '__all__'

class OMC34Nivel3Serializer(serializers.ModelSerializer):
    class Meta:
        model = OMC34Nivel3
        fields = '__all__'

class OMC34Nivel4Serializer(serializers.ModelSerializer):
    class Meta:
        model = OMC34Nivel4
        fields = '__all__'