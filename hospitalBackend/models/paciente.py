from django.db import models
from .usuario import Usuario
from .medico import Medico
from historiaClinica import HistoriaClinica
from enfermero import Enfermero
from familiar import Familiar

class Paciente(models.Model):
    id=models.AutoField(primary_key=True)
    usuario=models.ForeignKey(Usuario, related_name= 'paciente', on_delete=models.CASCADE)
    medico=models.ForeignKey(Medico, related_name= 'paciente', on_delete=models.CASCADE)
    enfermero=models.ForeignKey(Enfermero, related_name= 'paciente', on_delete=models.CASCADE)
    historiaClinica=models.ForeignKey(HistoriaClinica, related_name= 'paciente', on_delete=models.CASCADE)
    familiar=models.ForeignKey(Familiar, related_name= 'paciente', on_delete=models.CASCADE)
    
   