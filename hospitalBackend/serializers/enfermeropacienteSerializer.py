from rest_framework import serializers
from hospitalBackend.models.enfermeropaciente import EnfermeroPaciente

class EnfermeroPacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnfermeroPaciente
        fields = ['id', 'usuario', 'enfermero', 'paciente', 'cita', 'notas']