from django.db import models
from AutoParts.vehicle.models import EngineModel, VehicleModels, Manufacturer


class Part(models.Model):
    name = models.CharField(
        max_length=15,
    )

    picture = models.URLField()

    def __str__(self):
        return self.name


class Product(models.Model):
    part = models.ForeignKey(
        Part,
        on_delete=models.CASCADE,
    )
    engine = models.ForeignKey(
        EngineModel,
        on_delete=models.CASCADE,
    )
    vehicle_manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE,
    )
    part_manufacturer = models.CharField(
        max_length=15
    )
    logo = models.URLField()
    price = models.FloatField()
    quantity = models.IntegerField(
        default=0,
        null=True,
        blank=True,
    )

    description = models.CharField(
        max_length=200,
    )

    def __str__(self):
        return self.part.name

