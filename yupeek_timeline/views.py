from django.views.generic.base import TemplateView

from yupeek_timeline.models import Element, Timeline


class HomePage(TemplateView):
    template_name = 'homepage.html'

    def get_context_data(self, **kwargs):
        timelines = Timeline.objects.all()
        datas = []
        for timeline in timelines:
            name = timeline.title
            content = Element.objects.filter(timeline=timeline)
            datas.append({'title': name.lower(), 'content': content})
        return {'datas': datas}
