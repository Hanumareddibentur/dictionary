from django.urls import path
from dict import views

urlpatterns = [
    path('dict', views.home, name='home'),
]