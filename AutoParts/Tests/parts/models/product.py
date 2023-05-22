from django.test import TestCase

from AutoParts.parts.models import Part, Product
from AutoParts.vehicle.models import EngineModel, Manufacturer
from Tests.base.mixins import ProfileWithCarMixin
from Tests.base.tests import AutoPartsTestCase


class ProductTests(AutoPartsTestCase, ProfileWithCarMixin):

    def create_part(self, name='part', picture='picture'):
        return Part.objects.create(name=name, picture=picture)

    def create_product(self, part_manufacturer='manufacturer', logo='picture', price='1'):
        part = self.create_part()
        engine = EngineModel.objects.create(engine='1.8t')
        vehicle_manufacturer = Manufacturer.objects.create(name='Mercedes')
        return Product.objects.create(part=part, engine=engine, vehicle_manufacturer=vehicle_manufacturer,
                                      part_manufacturer=part_manufacturer, logo=logo, price=price)

    def test_part__if_new_part_is_created(self):
        products = list(Product.objects.all())
        self.assertEqual(0, len(products))
        self.create_product()
        products = list(Product.objects.all())
        self.assertEqual(1, len(products))
