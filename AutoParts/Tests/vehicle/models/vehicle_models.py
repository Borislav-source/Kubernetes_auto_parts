from django.utils.timezone import now

from AutoParts.vehicle.models import Manufacturer, EngineModel, VehicleModels
from Tests.base.tests import AutoPartsTestCase


class VehicleModelTest(AutoPartsTestCase):

    def crate_new_engine(self, engine='1.8t', power='225hp', engine_code='BAM'):
        return EngineModel.objects.create(engine=engine, power=power, engine_code=engine_code)

    def crate_new_vehicle_model(self, name='s3', image='image'):
        engine = self.crate_new_engine()
        return VehicleModels.objects.create(name=name, engine=engine, image_url=image, production_date=now())

    def test_manufacturer_model__if_new_brand_is_created(self):
        vehicle_models = list(VehicleModels.objects.all())
        self.assertEqual(0, len(vehicle_models))
        self.crate_new_vehicle_model()
        vehicle_models = list(VehicleModels.objects.all())
        self.assertEqual(1, len(vehicle_models))
        self.assertEqual('s3', vehicle_models[0].name)