from django.urls import path

from AutoParts.vehicle.views import VehicleManufacturersView, VehicleModelsView, VehicleEnginesView

urlpatterns = [
    path('cars/<str:_type>', VehicleManufacturersView.as_view(), name='cars'),
    path('car-models/<int:pk><str:_type>', VehicleModelsView.as_view(), name='car models'),
    path('car-model-engines/<int:model>', VehicleEnginesView.as_view(), name='vehicle engines'),
]
