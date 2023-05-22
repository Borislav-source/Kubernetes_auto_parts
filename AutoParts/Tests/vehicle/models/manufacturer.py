from AutoParts.vehicle.models import Manufacturer
from Tests.base.tests import AutoPartsTestCase


class ManufacturerModelTest(AutoPartsTestCase):

    def crate_new_manufacturer(self, name='Mercedes', image='image'):
        return Manufacturer.objects.create(name=name, image=image)

    def test_manufacturer_model__if_new_brand_is_created(self):
        manufacturers = list(Manufacturer.objects.all())
        self.assertEqual(0, len(manufacturers))
        self.crate_new_manufacturer()
        manufacturers = list(Manufacturer.objects.all())
        self.assertEqual(1, len(manufacturers))
        self.assertEqual('Mercedes', manufacturers[0].name)