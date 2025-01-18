from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path("", views.home_page_view, name="index"),
    path("contact", views.contact_page_view, name="contact"),
    path("now", views.now_page_view, name="now"),
    path("social", views.social_page_view, name="social"),
    path("work", views.work_page_view, name="work"),
    path("projects", views.project_list_view, name="projects"),
    path("snippets", views.snippet_list_view, name="snippets"),
    path("blog", views.blog_list_view, name="blog"),
]

