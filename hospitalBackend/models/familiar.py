from django.db import models
from .usuario import Usuario

class Familiar(models.Model):
    id=models.AutoField(primary_key=True)
    usuario=models.ForeignKey(Usuario, related_name= 'familiar', on_delete=models.CASCADE)
    parentesco=models.CharField('Parentesco', max_length=50)
    
