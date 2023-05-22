from django.urls import reverse

from AutoParts.accounts.models import Profile
from AutoParts.store.models import Order
from Tests.base.tests import AutoPartsTestCase


class CartViewTest(AutoPartsTestCase):

    def test_cart_view__if_right_template_is_used_with_authenticated_user(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('cart'))

        self.assertTemplateUsed(response, 'store/cart.html')

    def test_cart_view__if_user_is_not_authenticated(self):
        response = self.client.get(reverse('cart'))
        messages = list(response.context['messages'])
        self.assertEqual('You need to be sign in', str(messages[0]))

    def test_cart_view__with_is_authenticated_user_and_no_orders(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('cart'))
        order = response.context['order']
        self.assertEqual(None, order)

    def test_cart_view__with_is_authenticated_user_and_orders(self):
        self.client.force_login(self.user)
        customer = Profile.objects.first()
        order = Order.objects.create(customer=customer, complete=False)

        response = self.client.get(reverse('cart'))
        self.assertEqual(order, response.context['order'])