from django.contrib.auth import get_user_model
from AutoParts.account_auth.models import SiteUser
from Tests.base.tests import AutoPartsTestCase

UserModel = get_user_model()


class SiteUserTest(AutoPartsTestCase):

    def test_site_user__create_new_user(self):
        user = self.user
        self.assertTrue(isinstance(user, SiteUser))
        self.assertEqual('test@email.com', user.email)
