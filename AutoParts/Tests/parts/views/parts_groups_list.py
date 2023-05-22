from django.urls import reverse
from AutoParts.parts.models import Part
from Tests.base.mixins import ProfileWithCarMixin
from Tests.base.tests import AutoPartsTestCase


class PartsGroupsListTest(AutoPartsTestCase, ProfileWithCarMixin):

    def test_parts_groups_list__if_the_right_template_is_used(self):
        vehicle = ProfileWithCarMixin.vehicle
        response = self.client.get(reverse('parts groups list', kwargs={
            'engine': vehicle.model.engine.id
        }))
        self.assertTemplateUsed(response, 'parts/parts-groups-list.html')

    def test_parts_groups_list__if_right_parts_are_visualised(self):
        part_1 = Part.objects.create(name='part1')
        part_2 = Part.objects.create(name='part2')
        response = self.client.get(reverse('parts groups list', kwargs={
            'engine': ProfileWithCarMixin.vehicle.model.engine.id,
        }))
        parts = list(response.context['parts'])
        self.assertEqual(len(parts), 2)
        self.assertEqual(parts[0].name, 'part1')
        self.assertEqual(parts[1].name, 'part2')