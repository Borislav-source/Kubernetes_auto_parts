from django.utils.timezone import now

from AutoParts.accounts.models import Profile
from AutoParts.parts.models import Part, Product
from AutoParts.store.models import Order, OrderItem, ShippingAddress
from AutoParts.vehicle.models import EngineModel, Manufacturer
from Tests.base.tests import AutoPartsTestCase


class ShippingAddressTests(AutoPartsTestCase):
    def create_new_order(self):
        customer = Profile.objects.get(pk=self.user)
        return Order.objects.create(customer=customer, date_ordered=now())

    def create_new_shippingAddress(self, address='address', city='city', country='country', zipcode='zipcode',
                                   date_added=now()):
        customer = Profile.objects.get(pk=self.user)
        return ShippingAddress.objects.create(customer=customer, address=address, city=city, country=country,
                                              zipcode=zipcode,
                                              date_added=date_added)

    def test_order_model_if_new_order_is_created(self):
        shipping_addresses = list(ShippingAddress.objects.all())
        self.assertEqual(0, len(shipping_addresses))
        self.create_new_shippingAddress()
        shipping_addresses = list(ShippingAddress.objects.all())
        self.assertEqual(1, len(shipping_addresses))
