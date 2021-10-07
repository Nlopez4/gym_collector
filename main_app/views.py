from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.http import HttpResponse

class Home(TemplateView):
    template_name = "home.html"
    
class About(TemplateView):
    template_name = "about.html"
    

# other
class GymsList(TemplateView):
    template_name = "artist_list.html"