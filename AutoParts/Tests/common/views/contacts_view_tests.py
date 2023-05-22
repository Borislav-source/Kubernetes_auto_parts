from django.urls import reverse

from Tests.base.tests import AutoPartsTestCase


class ContactsViewTests(AutoPartsTestCase):

    def test_contacts_view__if_the_right_template_is_used(self):
        response = self.client.get(reverse('contacts'))
        self.assertTemplateUsed(response, 'pages/contacts.html')