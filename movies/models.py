from django.db import models

class Gore(models.Model):
    Nombre = models.CharField(max_length=40, null=False)
    Año_de_Publicación = models.IntegerField(null=False)
    Director = models.CharField(max_length=40, null=False)
    País = models.CharField(max_length=40, null=False)
    Género = models.CharField(max_length=40, null=False)
    Sinopsis = models.TextField(max_length=500, null=False)
    Picture = models.ImageField(upload_to="movies_images", null=True)
    TrailerURL = models.CharField(max_length=100, null=True)
    Duracion = models.IntegerField(null=True)  # en minutos
    Clasificacion = models.CharField(max_length=10, null=True)
    Rating = models.FloatField(null=True)
    Tags = models.CharField(max_length=100, null=True)
    
    def __str__(self):
        return self.Nombre
    
        
    