from rest_framework import serializers
from hospitalBackend.models.familiar import Familiar

class FamiliarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Familiar
        fields = ['id', 'usuario', 'parentesco']