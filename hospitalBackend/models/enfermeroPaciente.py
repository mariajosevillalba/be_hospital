from django.db import models
from .enfermero import Enfermero
from paciente import Paciente




class EnfermeroPaciente(models.Model):
    id=models.AutoField(primary_key=True)
    enfermero=models.ForeignKey(Enfermero, related_name= 'enfermeroPaciente', on_delete=models.CASCADE)
    paciente=models.ForeignKey(Paciente, related_name= 'enfermeroPaciente', on_delete=models.CASCADE)
    citas=models.TimeField('Citas')
    notas=models.TextField('Notas',blank=True)
   