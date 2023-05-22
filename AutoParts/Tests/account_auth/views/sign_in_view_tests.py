from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.models import User
from django.urls import reverse

from Tests.base.tests import AutoPartsTestCase

UserModel = get_user_model()


class SignInTest(AutoPartsTestCase):

    def test_sign_in__if_right_template_is_used(self):
        response = self.client.get(reverse('sign in'))
        self.assertTemplateUsed(response, 'pages/sign-in.html')

    def test_correct(self):
        user = authenticate(username=self.user_email, password=self.user_password)
        self.assertTrue((user is not None) and user.is_authenticated)

    def test_wrong_username(self):
        user = authenticate(username='wrong', password=self.user_password)
        self.assertFalse(user is not None and user.is_authenticated)

    def test_wrong_password(self):
        user = authenticate(username=self.user_email, password='wrong')
        self.assertFalse(user is not None and user.is_authenticated)
