from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views import View
from .models import gyms
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse
from django.shortcuts import redirect


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

    def get_success_url(self):
        return reverse('gyms_detail', kwargs={'pk': self.object.pk})


class GymsDetail(DetailView):
    model = gyms
    template_name = "gyms_detail.html"


class GymsUpdate(UpdateView):
    model = gyms
    fields = ['name', 'img', 'type', 'classes']
    template_name = "gyms_update.html"

    def get_success_url(self):
        return reverse('gyms_detail', kwargs={'pk': self.object.pk})


class GymsDelete(DeleteView):
    model = gyms
    template_name = "gyms_delete_confirmation.html"
    success_url = "/gyms/"


# class ClassCreate(View):

#     def post(self, request, pk):
#         type = request.POST.get("type")
#         description = request.POST.get("time")
#         gym = gyms.objects.get(pk=pk)
#         Class.objects.create(type=type, time=time, gym=gym)
#         return redirect('gyms_detail', pk=pk)
