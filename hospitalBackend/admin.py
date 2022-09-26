from django.contrib import admin
from be_hospital.hospitalBackend.models import familiar

from be_hospital.hospitalBackend.models.enfermero import Enfermero
from be_hospital.hospitalBackend.models.enfermeroPaciente import EnfermeroPaciente
from be_hospital.hospitalBackend.models.historiaClinica import HistoriaClinica
from .models.usuario import Usuario
from .models.medico import Medico
from .models.paciente import Paciente
from.models.familiar import Familiar
# Register your models here.

admin.site.register(Usuario)
admin.site.register(Medico)
admin.site.register(Paciente)
admin.site.register(Enfermero)
admin.site.register(HistoriaClinica)
admin.site.register(EnfermeroPaciente)
admin.site.register(Familiar)



