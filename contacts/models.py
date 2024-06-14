from django.db import models

# Create your models here.

from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name
    

# Create your models here.
class Incidencia(models.Model):
    departament = models.CharField(max_length=100)
    email = models.EmailField()
    descripcio = models.CharField(max_length=500)

    def __str__(self):
        return self.name