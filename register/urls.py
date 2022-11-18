from django.urls import path
from register import views

urlpatterns = [
    path("register", views.register_request, name="register"),
    path("", views.login_request, name="login"),
]