from django.db import models
from .usuario import Usuario
from .paciente import Paciente
from .enfermero import Enfermero

class EnfermeroPaciente(models.Model):
    id=models.AutoField(primary_key=True)
    usuario=models.ForeignKey(Usuario, related_name= 'enfermero_paciente', on_delete=models.CASCADE)
    enfermero=models.ForeignKey(Enfermero, related_name= 'enfermero_paciente', on_delete=models.CASCADE)
    paciente=models.ForeignKey(Paciente, related_name= 'enfermero_paciente', on_delete=models.CASCADE)
    cita=models.TimeField('Hora Cita', blank=True)
    notas=models.TextField('Notas', blank=True)
