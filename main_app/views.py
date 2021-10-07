from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import gyms
from django.views.generic.edit import CreateView


class Home(TemplateView):
    template_name = "home.html"


class About(TemplateView):
    template_name = "about.html"


# other
class GymsList(TemplateView):
    template_name = "gyms_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["gyms"] = gyms.objects.filter(name__icontains=name)
            # We add a header context that includes the search param
            context["header"] = f"Searching for {name}"
        else:
            context["gyms"] = gyms.objects.all()
            # default header for not searching
            context["header"] = "Local Gyms"
        return context


class GymsCreate(CreateView):
    model = gyms
    fields = ['name', 'img', 'type', 'classes']
    template_name = "gyms_create.html"
    success_url = "/gyms/"
