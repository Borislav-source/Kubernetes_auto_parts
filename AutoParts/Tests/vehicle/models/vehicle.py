from django.utils.timezone import now

from AutoParts.vehicle.models import Manufacturer, EngineModel, VehicleModels, Vehicle
from Tests.base.tests import AutoPartsTestCase


class VehicleTest(AutoPartsTestCase):

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

    def test_manufacturer_model__if_new_brand_is_created(self):
        vehicles = list(Vehicle.objects.all())
        self.assertEqual(0, len(vehicles))
        self.create_new_vehicle()
        vehicles = list(Vehicle.objects.all())
        self.assertEqual(1, len(vehicles))
        self.assertEqual('s3', vehicles[0].model.name)
