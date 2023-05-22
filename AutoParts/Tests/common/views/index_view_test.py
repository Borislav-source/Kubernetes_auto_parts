from django.urls import reverse

from Tests.base.tests import AutoPartsTestCase


class IndexViewTest(AutoPartsTestCase):

    def test_index_view__if_the_right_template_is_used(self):
        response = self.client.get(reverse('index'))
        self.assertTemplateUsed(response, 'pages/index.html')
