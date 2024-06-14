from django.contrib import admin

# Register your models here.
from .models import Contact, Incidencia

admin.site.register(Contact)
admin.site.register(Incidencia)