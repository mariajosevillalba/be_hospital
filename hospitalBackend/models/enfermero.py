from django.db import models
from .usuario import Usuario

class Enfermero(models.Model):
    id=models.AutoField(primary_key=True)
    usuario=models.ForeignKey(Usuario, related_name= 'enfermero', on_delete=models.CASCADE)
    area=models.CharField('Area', max_length=50)
    #auxiliar=models.CharField('Auxiliar', max_length=50)
