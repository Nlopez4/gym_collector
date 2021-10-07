from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import gyms


class Home(TemplateView):
    template_name = "home.html"


class About(TemplateView):
    template_name = "about.html"


# other
class GymsList(TemplateView):
    template_name = "gyms_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Here we are using the model to query the database for us.
        context["gyms"] = gyms.objects.all()
        return context
