from rest_framework import serializers
from UNIDADESMEDIDA.models import *

class TipoUniMedSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoUniMed
        fields = '__all__'

class SubTipUniSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubTipUni
        fields = '__all__'

class UnidadesMedidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnidadesMedida
        fields = '__all__'

