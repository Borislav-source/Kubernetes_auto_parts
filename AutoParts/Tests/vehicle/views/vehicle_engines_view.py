from django.urls import reverse
from django.utils.timezone import now
from AutoParts.vehicle.models import Manufacturer, Vehicle, VehicleModels, EngineModel
from Tests.base.mixins import ProfileWithCarMixin
from Tests.base.tests import AutoPartsTestCase


class VehicleEnginesViewTests(AutoPartsTestCase, ProfileWithCarMixin):

    def test_vehicle_engines_view__if_the_right_template_is_used(self):
        manufacturer = Manufacturer.objects.create(name='Mercedes', image='something')
        response = self.client.get(reverse('vehicle engines', kwargs={
            'model': manufacturer.id,
        }))

        self.assertTemplateUsed(response, 'vehicles/vehicle-list-by-engine.html')

    def test_vehicle_engines_view__if_the_manufacturers_are_visualised(self):
        manufacturer = Manufacturer.objects.create(name='Mercedes', image='something')
        engine = EngineModel.objects.create(engine='1.8t')
        vehicle_model = VehicleModels.objects.create(name='C-class', engine=engine, production_date=now())
        vehicle = Vehicle.objects.create(vehicle_type='Car', manufacturer=manufacturer, model=vehicle_model)
        response = self.client.get(reverse('vehicle engines', kwargs={
            'model': manufacturer.id,
        }))
        engine = response.context['engine_list'][0]
        self.assertEqual('1.8t', engine.engine)
