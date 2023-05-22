from django.utils.timezone import now
from AutoParts.accounts.models import Profile
from AutoParts.vehicle.models import EngineModel, Manufacturer, VehicleModels, Vehicle


class ProfileWithCarMixin:
    engine = EngineModel.objects.create(engine='1.8t')
    vehicle_manufacturer = Manufacturer.objects.create(name='Mercedes')
    vehicle_model = VehicleModels.objects.create(name='C-class', engine=engine, production_date=now())
    vehicle = Vehicle.objects.create(manufacturer=vehicle_manufacturer, vehicle_type='Car', model=vehicle_model)

    def tearDown(self):
        self.vehicle.delete()
