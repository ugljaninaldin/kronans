from django.urls import path
from . import views

app_name = "main"
urlpatterns = [
        path("", views.home, name="home"),
        path("team", views.team, name="team"),
        path("contact", views.contact, name="contact"),
        ]
