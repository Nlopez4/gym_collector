from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about/"),

    # other
    path('gyms/', views.GymsList.as_view(), name="gyms_list"),
    path('gyms/new/', views.GymsCreate.as_view(), name="gyms_create"),
    path('gyms/<int:pk>/', views.GymsDetail.as_view(), name="gyms_detail")

]
