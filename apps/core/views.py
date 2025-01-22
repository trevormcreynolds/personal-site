from django.shortcuts import render

from blog.models import Post


def home_page_view(request):
    posts = Post.published.all().order_by("-publish")[:3]
    return render(request, "pages/index.html", {"posts": posts})


def contact_page_view(request):
    return render(request, "pages/contact.html")


def about_page_view(request):
    return render(request, "pages/about.html")


def work_page_view(request):
    return render(request, "pages/work.html")


def project_list_view(request):
    return render(request, "pages/project_list.html")


def snippet_list_view(request):
    return render(request, "pages/snippet_list.html")
