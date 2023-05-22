from django.views.generic import TemplateView
from AutoParts.vehicle.models import Vehicle, VehicleModels, Manufacturer


class VehicleManufacturersView(TemplateView):
    template_name = 'vehicles/vehicle-list-by-manufacturers.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = kwargs['_type']
        context['manufacturers'] = Manufacturer.objects.all()
        return context


class VehicleModelsView(TemplateView):
    template_name = 'vehicles/vehicle-list-by-models.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = kwargs['pk']
        _type = kwargs['_type']
        context['vehicles'] = Vehicle.objects.filter(manufacturer_id=pk, vehicle_type=_type)
        return context


class VehicleEnginesView(TemplateView):
    template_name = 'vehicles/vehicle-list-by-engine.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        model = kwargs['model']
        vehicles = VehicleModels.objects.filter(pk=model)
        context['engine_list'] = [v.engine for v in vehicles]
        return context
