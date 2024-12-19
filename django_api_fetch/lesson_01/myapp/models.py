from django.db import models

# Create your models here.
class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length= 255)
    image = models.URLField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    brand = models.CharField(max_length=255)
    model= models.CharField(max_length=255)
    color = models.CharField(max_length=255, blank=True)
    category= models.CharField(max_length=255)
    discount = models.FloatField()

    def __str__(self):
        return self.title