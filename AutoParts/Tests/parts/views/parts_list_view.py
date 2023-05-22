from django.urls import reverse
from AutoParts.parts.models import Part, Product
from AutoParts.vehicle.models import Manufacturer, EngineModel
from Tests.base.mixins import ProfileWithCarMixin
from Tests.base.tests import AutoPartsTestCase


class PartsListViewTest(AutoPartsTestCase, ProfileWithCarMixin):
    def test_parts_list__if_the_right_template_is_used(self):
        vehicle = ProfileWithCarMixin.vehicle
        part = Part.objects.create(name='part')
        response = self.client.get(reverse('parts list', kwargs={
            'engine_id': vehicle.model.engine.id,
            'part_id': part.id
        }))
        self.assertTemplateUsed(response, 'parts/parts-list.html')

    def test_parts_list__if_right_products_are_visualised(self):
        manufacturer = Manufacturer.objects.create(name='aa')
        engine = EngineModel.objects.create(engine='2.0')
        part = Part.objects.create(name='part')
        product = Product.objects.create(
            part=part,
            engine=engine,
            vehicle_manufacturer=manufacturer,
            part_manufacturer='someone',
            price=5,
        )
        print(Product.objects.all())

        response = self.client.get(reverse('parts list', kwargs={
            'engine_id': engine.id,
            'part_id': part.id
        }))
        products = list(response.context['enrollments'])
        self.assertEqual(len(products), 1)
