from django.urls import reverse
from django.utils.timezone import now

from AutoParts.accounts.models import Profile
from AutoParts.vehicle.models import Vehicle, VehicleModels, Manufacturer, EngineModel
from Tests.base.tests import AutoPartsTestCase


class GarageViewTests(AutoPartsTestCase):

    def crate_new_engine(self, engine='1.8t', power='225hp', engine_code='BAM'):
        return EngineModel.objects.create(engine=engine, power=power, engine_code=engine_code)

    def crate_new_manufacturer(self, name='Mercedes', image='image'):
        return Manufacturer.objects.create(name=name, image=image)

    def crate_new_vehicle_model(self, name='s3', image='image'):
        engine = self.crate_new_engine()
        return VehicleModels.objects.create(name=name, engine=engine, image_url=image, production_date=now())

    def create_new_vehicle(self, _type='Car'):
        manufacturer = self.crate_new_manufacturer()
        vehicle_model = self.crate_new_vehicle_model()
        return Vehicle.objects.create(vehicle_type=_type, manufacturer=manufacturer, model=vehicle_model)

    def test_garage_view___with_authenticated_user_and_car_if_the_right_template_is_used(self):
        self.client.force_login(self.user)
        vehicle = self.create_new_vehicle()
        profile = Profile.objects.get(pk=self.user)
        profile.car = vehicle
        profile.save()
        response = self.client.get(reverse('garage'))
        self.assertTemplateUsed(response, 'pages/garage.html')
        self.assertEqual(vehicle, response.context['car'])

    def test_garage_view__with_Unauthenticated_user(self):
        response = self.client.get(reverse('garage'))
        messages = list(response.context['messages'])
        self.assertEqual('You need to be sign in!', str(messages[0]))

    def test_garage_view__with_authenticated_user_with_no_car(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('garage'))
        messages = list(response.context['messages'])
        self.assertEqual('You haven\'t add a car in Your profile.', str(messages[0]))

