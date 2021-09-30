from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import *
# Register your models here.
class resourceVeterinaria(resources.ModelResource):
    class Meta:
        model = veterinaria

class AdminVeterinaria(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ['nombre','ubicacion','correo','telefono']
    resource_class = resourceVeterinaria

admin.site.register(veterinaria, AdminVeterinaria)

class resourceServicios(resources.ModelResource):
    class Meta:
        model = servicios

class AdminServicios(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ['pk_producto','nombre','descripcion','precio']
    resource_class = resourceServicios

admin.site.register(servicios, AdminServicios)

class resourceMascota(resources.ModelResource):
    class Meta:
        model = mascota

class AdminMascota(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ['nombre_mascota','raza','color','edad', 'fk_servicios']
    resource_class = resourceVeterinaria

admin.site.register(mascota, AdminMascota)