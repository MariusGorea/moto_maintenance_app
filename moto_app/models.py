from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models


class Owner(models.Model):
    name = models.CharField(max_length=100, default="no name")
    position = models.CharField(max_length=100)
    personal_info = models.TextField()
    email = models.EmailField(null=True, blank=True)
    link = models.URLField(null=True, blank=True)

    def __str__(self):
        return f'{self.name}'


class Motorycycle(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, blank=True, null=True)
    motorcycle_brand = models.CharField(max_length=100, blank=True, null=True)
    motorcycle_model = models.CharField(max_length=100, default="")
    image = models.ImageField(upload_to='static/product_images/', default='static/not_available.png')
    vin = models.CharField(max_length=17)
    manufactured_year = models.IntegerField(default=2000)
    real_km = models.IntegerField(default=0)  # de introdus si data
    actual_km = models.IntegerField(default=0)
    next_maintenance = models.IntegerField(default=0)  # de introdus si data

    # parts_from_maintenance = models.IntegerField(default=0)
    # parts_from_repairs = models.IntegerField(default=0)

    def next_maintenance(self):
        return 10000 + self.real_km


class Service(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, blank=True, null=True)
    logo = models.ImageField(upload_to='static/product_images/', default='static/not_available.png')


class Part(models.Model):
    UMS = (('l', 'l'), ('buc', 'pcs'), ('kg', 'kg'), ('hr', 'hr'),)
    name = models.CharField(max_length=255)
    item_code = models.CharField(max_length=255)
    unit_measurement = models.CharField(max_length=20, choices=UMS)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.name} {self.price}'


class SoldPart(models.Model):
    part = models.ForeignKey(Part, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    motorcycle = models.ForeignKey(Motorycycle, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.part}'


#de creat Motorcycle List pt administrator