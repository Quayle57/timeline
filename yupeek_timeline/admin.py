from django.contrib import admin

# Register your models here.
from yupeek_timeline.models import Timeline, Element

admin.site.register(Timeline)
admin.site.register(Element)
