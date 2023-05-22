from django.test import TestCase

from AutoParts.common.models import SiteInformation


class SiteInformationTest(TestCase):

    def create_site_information(self, phone='000', address='address', email='information@email.com',
                                facebook='facebook'):
        return SiteInformation.objects.create(phone=phone, email=email, address=address, facebook=facebook)

    def test_site_information__if_new_information_is_added(self):
        information = self.create_site_information()
        self.assertTrue(isinstance(information, SiteInformation))
        self.assertEqual('000', information.phone)
