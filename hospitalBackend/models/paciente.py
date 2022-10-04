from django.db import models
from .usuario import Usuario
from .medico import Medico
from .historia import Historia
from .familiar import Familiar
from .enfermero import Enfermero


class Paciente(models.Model):
    id=models.AutoField(primary_key=True)
    usuario=models.ForeignKey(Usuario, on_delete=models.CASCADE)
    medico=models.ForeignKey(Medico, on_delete=models.CASCADE)
    enfermero=models.ForeignKey(Enfermero, related_name= 'paciente', on_delete=models.CASCADE, null=True) 
    historia=models.ForeignKey(Historia, related_name= 'paciente', on_delete=models.CASCADE, null=True) 
    familiar=models.ForeignKey(Familiar, related_name= 'paciente', on_delete=models.CASCADE, null=True)

    
   