from rest_framework import serializers
from hospitalBackend.models.historia import Historia

class HistoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Historia
        fields = ['id', 'usuario', 'rh', 'f_respiratoria', 'f_cardiaca', 'temperatura', 'presion_arterial', 'glicemias', 'diagnostico', 'cuidados']
        