from django.db import models

# Create your models here.
class NestGuard(models.Model):
    titulo = models.CharField(max_length=50)
    descricao1 = models.TextField(max_length=1500)
    descricao2 = models.TextField(max_length=1500)
    descricao3 = models.TextField(max_length=1500)
    logoNavbarEscuro = models.ImageField(upload_to='logoNavbarEscuro/')
    logoNavbarClaro = models.ImageField(upload_to='logoNavbarClaro/')
    logoGrandeEscuro = models.ImageField(upload_to='logoGrandeEscuro/')
    logoGrandeClaro = models.ImageField(upload_to='logoGrandeClaro/')


    def __str__(self):
        return self.titulo
    
    