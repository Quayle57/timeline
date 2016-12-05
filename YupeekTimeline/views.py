from django.views.generic.base import TemplateView

from YupeekTimeline.models import Element


class HomePage(TemplateView):
    template_name = 'homepage.html'

    def get_context_data(self, **kwargs):
        prod = Element.objects.filter(type="Prod")
        staging = Element.objects.filter(type="Staging")
        return {"prod": prod, "staging": staging}
