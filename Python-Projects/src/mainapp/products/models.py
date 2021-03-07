from django.db import models

# Create your models here.
class Product(models.Model):
    type = models.CharField(max_length=60)
    name = models.CharField(max_length=60, default="", blank=True, null=False)
    description = models.TextField(max_length=300, default="", blank=True)
    price = models.DecimalField(default=0.00, max_digit=1000, decimal_places=2)
    image = models.CharField(max_length=255, default='', blank=True)

    objects = models.Manager()

    def__str__(self):
        return self.name