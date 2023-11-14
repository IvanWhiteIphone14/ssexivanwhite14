from django.db import models

from django.db import models
from django.template.defaultfilters import floatformat


class Car(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    price = models.CharField(max_length=10)
    short_info = models.TextField(default='short info')
    fuel = models.TextField(default='N/A')
    traction = models.TextField(default='N/A')
    gearbox = models.TextField(default='Automatic')
    engine = models.TextField(default='N/A')
    year = models.IntegerField()
    main_photo = models.ImageField(upload_to='taciki/', default='default_photo.jpg')
    type = models.CharField(max_length=100, default='Coupe')

    def uprice(self):
        # Remove space and convert price to integer
        price_without_space = self.price.replace(' ', '')
        price_as_int = int(price_without_space)
        # Calculate uprice * 1.2 and format it to have 0 decimal places
        return floatformat(price_as_int * 1.2, 0)

    def __str__(self):
        return f"{self.brand} {self.model} {self.type}({self.year}) {self.engine}"


class CarPhoto(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='car_photos/')

# Create your models here.
