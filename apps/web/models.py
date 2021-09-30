from django.db import models

# Create your models here.

class veterinaria(models.Model):
    pk_Veterinaria = models.AutoField(primary_key=True, null=False, blank=False)
    nombre = models.CharField(max_length=20, null=False, blank=False)
    ubicacion = models.TextField(null=False, blank=False)
    correo = models.CharField(max_length=30, null=False, blank=False)
    telefono = models.CharField(max_length=8, null=False, blank=False)

    class Meta:
        verbose_name = 'veterinaria'
        verbose_name_plural = 'veterinarias'
        ordering = ['nombre']

    def __str__(self):
        return "{0}".format(self.nombre)

class servicios(models.Model):
    pk_producto = models.AutoField(primary_key=True, null=False, blank=False)
    nombre = models.CharField(max_length=20, null=False, blank=False)
    descripcion = models.TextField(null=False, blank=False)
    precio = models.IntegerField(null=False, blank=False)
    imagen = models.URLField(max_length=8000, blank=False, null=False, default='https://cdn.euroinnova.edu.es/img/subidasEditor/11-1596082251.jpg')

    class Meta:
        verbose_name = 'servicios'
        verbose_name_plural = 'servicioss'
        ordering = ['nombre']

    def __str__(self):
        return "{0}".format(self.nombre)

class mascota(models.Model):
    pk_mascota = models.AutoField(primary_key=True, null=False, blank=False)
    nombre_mascota = models.CharField(max_length=25, null=False, blank=False)
    raza = models.CharField(max_length=20, null=False, blank=False)
    color = models.CharField(max_length=50, null=False, blank=False)
    edad = models.CharField(max_length=10, null=False, blank=False)
    fk_servicios = models.ForeignKey(servicios, null=False, blank=False, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'mascota'
        verbose_name_plural = 'mascotas'
        ordering = ['nombre_mascota']

    def __str__(self):
        return "{0}".format(self.nombre_mascota)



