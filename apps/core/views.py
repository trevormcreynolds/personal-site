from django.shortcuts import render


def home_page_view(request):
    return render(request, "pages/index.html")

def contact_page_view(request):
    return render(request, "pages/contact.html")

def now_page_view(request):
    return render(request, "pages/now.html")

def social_page_view(request):
    return render(request, "pages/social.html")

def work_page_view(request):
    return render(request, "pages/work.html")

def project_list_view(request):
    return render(request, "pages/project_list.html")

def snippet_list_view(request):
    return render(request, "pages/snippet_list.html")

def blog_list_view(request):
    return render(request, "pages/blog_list.html")