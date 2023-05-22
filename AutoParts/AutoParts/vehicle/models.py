from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(
        max_length=15,
    )
    image = models.FileField(
        upload_to='Manufacturers'
    )

    def __str__(self):
        return self.name


class EngineModel(models.Model):
    engine = models.CharField(
        max_length=10,
    )
    power = models.CharField(
        max_length=10,
    )
    engine_code = models.CharField(
        max_length=100,
    )

    def __str__(self):
        return self.engine


class VehicleModels(models.Model):
    name = models.CharField(
        max_length=15,
    )
    engine = models.ForeignKey(
        EngineModel,
        on_delete=models.CASCADE
    )
    image_url = models.URLField()
    production_date = models.DateTimeField()

    def __str__(self):
        return self.name


class Vehicle(models.Model):
    ALL_CHOICES = (
        ('Car', 'Car'),
        ('Truck', 'Truck'),
        ('Motorcycle', 'Motorcycle'),
    )

    vehicle_type = models.CharField(
        max_length=25,
        choices=ALL_CHOICES,
    )
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE
    )
    model = models.ForeignKey(
        VehicleModels,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.manufacturer} {self.model}'
