from django.views.generic.base import TemplateView

from YupeekTimeline.models import Element


class HomePage(TemplateView):
    template_name = 'homepage.html'

    def get_context_data(self, **kwargs):
        elems = Element.objects.all()
        return {"elements": elems}
