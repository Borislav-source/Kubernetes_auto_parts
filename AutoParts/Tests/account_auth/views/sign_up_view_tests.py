from django.contrib.auth import get_user_model
from django.urls import reverse
from AutoParts.accounts.models import Profile
from Tests.base.tests import AutoPartsTestCase

UserModel = get_user_model()


class SignUpTests(AutoPartsTestCase):

    def test_sign_up__if_right_template_is_used(self):
        response = self.client.get(reverse('sign up'))
        self.assertTemplateUsed(response, 'pages/sign-up.html')

    def test_sign_up__if_new_user_is_created(self):
        new_user = UserModel.objects.create_user(email='new@user.com', password='newPassword')
        existing_user = UserModel.objects.filter(email='new@user.com')
        self.assertTrue(existing_user)

    def test_sign_up__id_new_profile_is_created_with_new_user(self):
        new_user = UserModel.objects.create_user(email='new@user.com', password='newPassword')
        profile = Profile.objects.get(pk=new_user)
        self.assertTrue(profile)