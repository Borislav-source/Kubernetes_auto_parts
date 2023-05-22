from django.urls import path

from AutoParts.parts.views import PartsGroupsList, PartsListView

urlpatterns = [
    path('<int:engine>', PartsGroupsList.as_view(), name='parts groups list'),
    path('parts-list/<int:engine_id><int:part_id>', PartsListView.as_view(), name='parts list'),
]
