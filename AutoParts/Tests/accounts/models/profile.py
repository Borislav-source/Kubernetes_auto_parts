from django.test import TestCase

from AutoParts.accounts.models import Profile
from Tests.base.tests import AutoPartsTestCase


class ProfileTest(AutoPartsTestCase):

    def test_profile_model_if_a_new_profile_is_created_with_new_user_registration(self):
        profiles = list(Profile.objects.all())
        self.assertEqual(1, len(profiles))
        user2 = self.create_new_user()
        profiles = list(Profile.objects.all())
        self.assertEqual(2, len(profiles))

    def test_profile_model_if_the_profile_is_deleted_with_deleting_user(self):
        profiles = list(Profile.objects.all())
        self.assertEqual(1, len(profiles))
        self.user.delete()
        profiles = list(Profile.objects.all())
        self.assertEqual(0, len(profiles))


