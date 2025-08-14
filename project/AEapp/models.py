from django.db import models

# Create your models here.

class Product(models.Model):
    image = models.ImageField(upload_to='productImages/')
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    ingredients = models.CharField(max_length=1000)
    price = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name