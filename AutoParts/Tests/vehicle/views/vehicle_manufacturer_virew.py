from django.urls import reverse

from AutoParts.vehicle.models import Manufacturer
from Tests.base.mixins import ProfileWithCarMixin
from Tests.base.tests import AutoPartsTestCase


class VehicleManufacturersViewTests(AutoPartsTestCase, ProfileWithCarMixin):

    def test_vehicle_manufacturers__if_the_right_template_is_used(self):
        response = self.client.get(reverse('cars', kwargs={
            '_type': 'car'
        }))

        self.assertTemplateUsed(response, 'vehicles/vehicle-list-by-manufacturers.html')

    def test_vehicle_manufacturers__if_the_manufacturers_are_visualised(self):
        manufacturer = Manufacturer.objects.create(name='Mercedes', image='something')
        response = self.client.get(reverse('cars', kwargs={
            '_type': 'car'
        }))
        make = response.context['manufacturers'][0]
        self.assertEqual('Mercedes', make.name)