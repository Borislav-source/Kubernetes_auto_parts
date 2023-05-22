from django.contrib.auth import get_user_model
from django.db import models
from AutoParts.vehicle.models import Vehicle

UserModel = get_user_model()


class Profile(models.Model):
    first_name = models.CharField(
        max_length=20,
        blank=True,
        null=True,
    )
    last_name = models.CharField(
        max_length=20,
        blank=True,
    )
    profile_picture = models.ImageField(
        upload_to='profiles',
        blank=True,
    )
    age = models.IntegerField(
        blank=True,
        null=True,
    )
    is_done = models.BooleanField(
        default=False,
    )
    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    car = models.ForeignKey(
        Vehicle,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.first_name