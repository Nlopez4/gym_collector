from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about/"),

    # other
    path('gyms/', views.GymsList.as_view(), name="gyms_list"),
    path('gyms/new/', views.GymsCreate.as_view(), name="gyms_create"),
    path('gyms/<int:pk>/', views.GymsDetail.as_view(), name="gyms_detail"),
    path('gyms/<int:pk>/update',
         views.GymsUpdate.as_view(), name="gyms_update"),
    path('gyms/<int:pk>/delete',
         views.GymsDelete.as_view(), name="gyms_delete"),

]
