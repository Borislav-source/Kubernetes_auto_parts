from AutoParts.vehicle.models import Manufacturer, EngineModel
from Tests.base.tests import AutoPartsTestCase


class EngineModelTest(AutoPartsTestCase):

    def crate_new_engine(self, engine='1.8t', power='225hp', engine_code='BAM'):
        return EngineModel.objects.create(engine=engine, power=power, engine_code=engine_code)

    def test_manufacturer_model__if_new_brand_is_created(self):
        engines = list(EngineModel.objects.all())
        self.assertEqual(0, len(engines))
        self.crate_new_engine()
        engines = list(EngineModel.objects.all())
        self.assertEqual(1, len(engines))
        self.assertEqual('1.8t', engines[0].engine)