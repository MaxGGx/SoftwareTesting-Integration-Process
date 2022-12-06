from django.db import models

# Create your models here.

class receta(models.Model):
    nombreReceta = models.CharField(max_length = 300, verbose_name = "Nombre Receta", blank=False, null=False)
    ingredientes = models.TextField(verbose_name="Ingredientes Receta", blank=False, null=False)
    pasos = models.TextField(verbose_name="Pasos Receta", blank=False, null=False)
    imagenReceta = models.ImageField(verbose_name="Imagen Receta",upload_to='images/')
    autor = models.CharField(max_length = 30, verbose_name = "Autor Receta", blank=False, null=False)

    def __str__(self):
        return(str(self.nombreReceta))