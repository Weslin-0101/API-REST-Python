from django.contrib import admin
from core.models import Materias

# Register your models here.
class EventoAdmin(admin.ModelAdmin):
   list_display = ('nome', 'credito', 'codigo')

admin.site.register(Materias, EventoAdmin)
