from django.contrib.auth.models import User
from django.db import models
from AutoParts.accounts.models import Profile
from AutoParts.parts.models import Product


class Order(models.Model):
    customer = models.ForeignKey(
        Profile,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    date_ordered = models.DateTimeField(
        auto_now_add=True,
    )
    complete = models.BooleanField(
        default=False,
        null=True,
        blank=True,
    )
    transaction_id = models.CharField(
        max_length=200,
        null=True,
    )

    @property
    def get_total_for_cart(self):
        orderitems = self.orderitem_set.all()
        total = sum([o.get_total for o in orderitems])
        return total

    @property
    def get_quantity_of_cart(self):
        orderitems = self.orderitem_set.all()
        quantity = sum([item.quantity for item in orderitems])
        return quantity

    def __str__(self):
        return str(self.id)


class OrderItem(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    order = models.ForeignKey(
        Order,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    quantity = models.IntegerField(
        default=0,
        null=True,
        blank=True
    )
    date_added = models.DateTimeField(
        auto_now_add=True
    )

    @property
    def get_total(self):
        if self.product:
            total = self.product.price * self.quantity
            return total
        return 0


class ShippingAddress(models.Model):
    customer = models.ForeignKey(
        Profile,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    order = models.ForeignKey(
        Order,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    address = models.CharField(
        max_length=200,
        null=True,
    )
    city = models.CharField(
        max_length=200,
        null=True,
    )
    country = models.CharField(
        max_length=200,
        null=True,
    )
    zipcode = models.CharField(
        max_length=200,
        null=True,
    )
    date_added = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.address
