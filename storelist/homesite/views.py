# coding: utf-8
from django.views.generic import TemplateView


class HomeSiteView(TemplateView):
    template_name = 'homesite/index.html'
