from rest_framework import serializers
from . import models


class HistoriaSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'paciente', 'descripcion', 'examenes', 'medicamentos')
        model = models.Historia