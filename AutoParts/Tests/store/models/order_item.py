from django.utils.timezone import now

from AutoParts.accounts.models import Profile
from AutoParts.parts.models import Part, Product
from AutoParts.store.models import Order, OrderItem
from AutoParts.vehicle.models import EngineModel, Manufacturer
from Tests.base.tests import AutoPartsTestCase


class OrderItemTests(AutoPartsTestCase):
    def create_new_order(self):
        customer = Profile.objects.get(pk=self.user)
        return Order.objects.create(customer=customer, date_ordered=now())

    def create_part(self, name='part', picture='picture'):
        return Part.objects.create(name=name, picture=picture)

    def create_product(self, part_manufacturer='manufacturer', logo='picture', price='1'):
        part = self.create_part()
        engine = EngineModel.objects.create(engine='1.8t')
        vehicle_manufacturer = Manufacturer.objects.create(name='Mercedes')
        return Product.objects.create(part=part, engine=engine, vehicle_manufacturer=vehicle_manufacturer,
                                      part_manufacturer=part_manufacturer, logo=logo, price=price)

    def create_new_orderItem(self):
        product = self.create_product()
        order = self.create_new_order()
        return OrderItem.objects.create(product=product, order=order)

    def test_order_model_if_new_order_is_created(self):
        orderitems = list(OrderItem.objects.all())
        self.assertEqual(0, len(orderitems))
        self.create_new_orderItem()
        orderitems = list(Order.objects.all())
        self.assertEqual(1, len(orderitems))