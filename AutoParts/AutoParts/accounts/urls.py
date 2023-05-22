from django.urls import path

from AutoParts.accounts.views import ProfileDetailsView, change_profile_details

urlpatterns = [
    path('', ProfileDetailsView.as_view(), name='profile details'),
    path('account-change/', change_profile_details, name='change profile'),
]

