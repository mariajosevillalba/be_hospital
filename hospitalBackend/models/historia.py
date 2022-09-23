from django.db import models
from .usuario import Usuario

class Historia(models.Model):
    id=models.AutoField(primary_key=True)
    usuario=models.ForeignKey(Usuario, related_name= 'historia', on_delete=models.CASCADE)
    f_respiratoria=models.CharField('F.Respiratoria', max_length=50)
    f_cardiaca=models.CharField('F.Cardiaca', max_length=50)
    temperatura=models.CharField('Temperatura', max_length=50)
    presion_arterial=models.CharField('Presion Arterial', max_length=50)
    glicemias=models.CharField('Glicemias', max_length=50)
    diagnostico=models.CharField('Diagnostico', max_length=150)
    cuidados=models.CharField('Cuidados', max_length=1000)