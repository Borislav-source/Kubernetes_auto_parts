from django.views.generic import TemplateView, DetailView, ListView

from AutoParts.parts.models import Part, Product


class PartsGroupsList(TemplateView):
    template_name = 'parts/parts-groups-list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['engine_id'] = kwargs['engine']
        context['parts'] = Part.objects.all()
        return context


class PartsListView(TemplateView):
    template_name = 'parts/parts-list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        engine_id = kwargs['engine_id']
        part_id = kwargs['part_id']
        context['engine_id'] = engine_id
        context['part_id'] = part_id
        context['enrollments'] = Product.objects.filter(engine_id=engine_id, part_id=part_id)
        return context


def part_details(request):
    pass
