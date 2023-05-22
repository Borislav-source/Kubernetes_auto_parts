from django.urls import reverse
from AutoParts.accounts.models import Profile
from Tests.base.mixins import ProfileWithCarMixin
from Tests.base.tests import AutoPartsTestCase


class ProfileDetailsTest(AutoPartsTestCase, ProfileWithCarMixin):

    def test__profile_details_view_is_using_right_template(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('profile details'))
        self.assertTemplateUsed(response, 'pages/profile-details.html')

    def test__profile_details_logged_in_client_with_no_details(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('profile details'))

        self.assertEqual(self.user.id, response.context['profile'].user_id)
        self.assertEqual(None, response.context['profile'].car_id)
        self.assertEqual(None, response.context['profile'].first_name)
        self.assertEqual('', response.context['profile'].last_name)
        self.assertEqual(None, response.context['profile'].age)

    def test__profile_details_logged_in_client_change_profile_details(self):
        profile = Profile.objects.get(pk=self.user)
        profile.first_name = 'Borko'
        profile.last_name = 'Borko'
        profile.age = 1
        profile.profile_picture = 'file/profile_picture.img'
        profile.save()
        self.client.force_login(self.user)
        response = self.client.get(reverse('profile details'))
        self.assertEqual('Borko', response.context['profile'].first_name)
        self.assertEqual('Borko', response.context['profile'].last_name)
        self.assertEqual(1, response.context['profile'].age)
        self.assertEqual('file/profile_picture.img', response.context['profile'].profile_picture)

    def test__profile_details_logged_in_client_change_car_details(self):
        profile = Profile.objects.get(pk=self.user)
        profile.car = ProfileWithCarMixin.vehicle
        profile.save()
        self.client.force_login(self.user)
        response = self.client.get(reverse('profile details'))
        self.assertEqual(profile.car_id, response.context['profile'].car_id)

    def tearDown(self):
        self.user.delete()

