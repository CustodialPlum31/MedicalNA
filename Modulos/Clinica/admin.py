from django.contrib import admin
from Modulos.Clinica.models import *

# Register your models here.

admin.site.register(Medico)
admin.site.register(Paciente)
admin.site.register(Consulta)
admin.site.register(Expediente)
admin.site.register(Administrador)
admin.site.register(Estudio)
