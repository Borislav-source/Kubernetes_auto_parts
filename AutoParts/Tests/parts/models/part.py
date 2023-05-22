from django.test import TestCase

from AutoParts.parts.models import Part


class PartTests(TestCase):

    def create_part(self, name='part', picture='picture'):
        return Part.objects.create(name=name, picture=picture)

    def test_part__if_new_part_is_created(self):
        parts = list(Part.objects.all())
        self.assertEqual(0, len(parts))
        self.create_part()
        parts = list(Part.objects.all())
        self.assertEqual(1, len(parts))
