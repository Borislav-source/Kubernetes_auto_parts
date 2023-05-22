from django.urls import path, include
from AutoParts.common.views import IndexView, garage, ContactsView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('accounts/', include('AutoParts.account_auth.urls')),
    path('vehicles/', include('AutoParts.vehicle.urls')),
    path('garage/', garage, name='garage'),
    path('information/', ContactsView.as_view(), name='contacts'),
]