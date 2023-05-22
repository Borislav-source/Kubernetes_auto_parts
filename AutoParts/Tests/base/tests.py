from django.contrib.auth import get_user_model
from django.test import TestCase, Client

UserModel = get_user_model()


class AutoPartsTestCase(TestCase):
    user_email = 'test@email.com'
    user_password = 'test1234'

    def assertListEmpty(self, ll):
        return self.assertListEqual([], ll, 'The list is not empty')

    def setUp(self) -> None:
        self.client = Client()
        self.user = UserModel.objects.create_user(email=self.user_email, password=self.user_password)

    def create_new_user(self):
        self.new_user = UserModel.objects.create_user(email='new_user@email.com', password=self.user_password)
