
# Create your models here.

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Car(models.Model):
    producer = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    release_year = models.IntegerField(
        validators=[MinValueValidator(1920), MaxValueValidator(2020)], default=2020
    )
    MECHANIC = 'Mechanic'
    AUTOMATIC = 'Automatic'
    ROBOTIC = 'Robotic'
    TRANSMISSION = [
        (MECHANIC, 'mechanics'),
        (AUTOMATIC, 'automatic'),
        (ROBOTIC, 'robotic'),
    ]
    transmission = models.CharField(max_length=15, choices=TRANSMISSION, default=MECHANIC)
    image = models.ImageField(upload_to='static/images/cars_image/%Y/%m/%d', blank=True)
    color = models.CharField(max_length=150)
    