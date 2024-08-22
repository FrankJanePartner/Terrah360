from django.db import models

# Create your models here.
class Subscribers(models.Model):
    email = models.EmailField( max_length=254)

    def __str__(self):
        return f'{self.email}'
    
    class Meta:
        verbose_name_plural = "Subscribers"