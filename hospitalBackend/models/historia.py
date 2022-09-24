from django.db import models
from .usuario import Usuario

class Historia(models.Model):
    id=models.AutoField(primary_key=True)
    usuario=models.ForeignKey(Usuario, related_name= 'historia', on_delete=models.CASCADE)
    rh=models.CharField('Grupo Sanguíneo', max_length=150)
    f_respiratoria=models.DecimalField('F.Respiratoria', decimal_places=3,max_digits=3)
    f_cardiaca=models.DecimalField('F.Cardiaca', decimal_places=3,max_digits=3)
    temperatura=models.DecimalField('Temperatura', decimal_places=3,max_digits=3)
    presion_arterial=models.DecimalField('Presion Arterial', decimal_places=3,max_digits=3)
    glicemias=models.DecimalField('Glicemias', decimal_places=3,max_digits=3)
    diagnostico=models.CharField('Diagnostico', max_length=150)
    cuidados=models.CharField('Cuidados', max_length=1000)