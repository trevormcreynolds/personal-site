from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

import markdown

from .models import Post, BlogTag


def post_list_view(request, tag_slug=None):
    post_list = Post.published.all().order_by("-publish")
    tag = None

    if tag_slug:
        tag = get_object_or_404(BlogTag, slug=tag_slug)
        post_list = post_list.filter(tags__in=[tag])

    # Pagination with 3 posts per page
    paginator = Paginator(post_list, 3)
    page_number = request.GET.get("page", 1)

    try:
        posts = paginator.page(page_number)

    except PageNotAnInteger:
        # If page_number is not an integer, deliver the first page
        posts = paginator.page(1)

    except EmptyPage:
        # If page_number is out of range, deliver last page of results
        posts = paginator.page(paginator.num_pages)

    return render(request, "blog/post_list.html", {"posts": posts, "tag": tag})


def post_detail_view(request, post):
    post = get_object_or_404(Post, status=Post.Status.PUBLISHED, slug=post)
    post.body = markdown.markdown(post.body, extensions=['markdown.extensions.codehilite', "markdown.extensions.extra", "markdown.extensions.tables", "markdown.extensions.fenced_code",])

    return render(request, "blog/post_detail.html", {"post": post})
