from rest_framework import serializers
from hospitalBackend.models.enfermero import Enfermero

class EnfermeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enfermero
        fields = ['id', 'usuario', 'area', 'auxiliar',]