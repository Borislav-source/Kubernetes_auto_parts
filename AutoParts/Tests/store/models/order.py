from django.utils.timezone import now

from AutoParts.accounts.models import Profile
from AutoParts.store.models import Order
from Tests.base.tests import AutoPartsTestCase


class OrderTests(AutoPartsTestCase):
    def create_new_order(self):
        customer = Profile.objects.get(pk=self.user)
        return Order.objects.create(customer=customer, date_ordered=now())

    def test_order_model_if_new_order_is_created(self):
        orders = list(Order.objects.all())
        self.assertEqual(0, len(orders))
        self.create_new_order()
        orders = list(Order.objects.all())
        self.assertEqual(1, len(orders))