from django.contrib import admin
from .models.usuario import Usuario
from .models.medico import Medico
from .models.paciente import Paciente
from .models.enfermero import Enfermero
from .models.familiar import Familiar
from .models.historia import Historia
from .models.enfermeropaciente import EnfermeroPaciente

# Register your models here.

admin.site.register(Usuario)
admin.site.register(Medico)
admin.site.register(Paciente)
admin.site.register(Enfermero)
admin.site.register(Familiar)
admin.site.register(Historia)
admin.site.register(EnfermeroPaciente)

