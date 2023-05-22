from django.contrib import admin

from AutoParts.vehicle.models import Vehicle, Manufacturer, VehicleModels, EngineModel

admin.site.register(Vehicle)
admin.site.register(Manufacturer)
admin.site.register(VehicleModels)
admin.site.register(EngineModel)
