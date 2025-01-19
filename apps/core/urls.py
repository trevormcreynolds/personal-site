from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path("", views.home_page_view, name="index"),
    path("contact", views.contact_page_view, name="contact"),
    path("about", views.about_page_view, name="about"),
    path("work", views.work_page_view, name="work"),
    path("projects", views.project_list_view, name="projects"),
    path("snippets", views.snippet_list_view, name="snippets"),
]
