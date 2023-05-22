from django.db import models


class SiteInformation(models.Model):
    phone = models.CharField(
        max_length=100,
    )
    address = models.CharField(
        max_length=100,
    )
    email = models.EmailField()
    facebook = models.CharField(
        max_length=50,
    )
