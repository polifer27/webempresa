from django.urls import path
from .import views

urlpatterns = [
    #paths de services
    path('', views.services, name="services"),
   
]