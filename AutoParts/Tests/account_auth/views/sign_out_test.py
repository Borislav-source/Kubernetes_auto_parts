from django.urls import reverse

from Tests.base.tests import AutoPartsTestCase


class SignOutTest(AutoPartsTestCase):

    def test_sign_out__if_user_is_logged_out(self):
        self.client.force_login(self.user)
        self.assertTrue(self.user)
        self.client.logout()
        self.assertTrue(self.user)




