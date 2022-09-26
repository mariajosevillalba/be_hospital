from django.db import models

class HistoriaClinica(models.Model):
    id=models.AutoField(primary_key=True)
    oximetria=models.DecimalField('Oximetria',max_digits=5, decimal_places=2)
    f_respiratoria= models.DecimalField('F_respiratoria',max_digits=5, decimal_places=2)
    f_cardiaca= models.DecimalField('F_cardiaca',max_digits=5, decimal_places=2)
    temperatura = models.DecimalField('Temperatura',max_digits=5, decimal_places=2)
    presion_arterial= models.DecimalField('Presion_arterial',max_digits=5, decimal_places=2)
    glicemias= models.DecimalField('Glicemias',max_digits=5, decimal_places=2)
    diagnostico=models.CharField('Diagnostico',max_length=100)
    cuidados=models.CharField('Cuidados',max_length=100)
    


#     CampoDecimal.max_digits
# El número máximo de dígitos permitidos en el número. Tenga en cuenta que este número debe ser mayor o igual que decimal_places.

# CampoDecimal.decimal_places
# El número de lugares decimales para almacenar con el número.

# Por ejemplo , para almacenar números hasta 999 con una resolución de 2 decimales, usaría:

# modelos.DecimalField(..., max_digits=5, decimal_places=2)