from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from blog.constants import POSTS_ON_HOME_PAGE
from blog.models import Category, Post


def get_published_posts():
    return Post.objects.select_related(
        'category', 'location', 'author'
    ).filter(
        pub_date__lte=timezone.now(),
        is_published=True,
        category__is_published=True
    )


def index(request: HttpRequest) -> HttpResponse:
    """Отображает главную страницу блога со списком всех постов."""
    post_list = get_published_posts()[:POSTS_ON_HOME_PAGE]
    context = {'post_list': post_list}
    return render(request, 'blog/index.html', context)


def post_detail(request: HttpRequest, post_id: int) -> HttpResponse:
    """Отображает детальную страницу поста по его ID."""
    post = get_object_or_404(get_published_posts(), id=post_id)
    context = {'post': post}
    return render(request, 'blog/detail.html', context)


def category_posts(request: HttpRequest, category_slug: str) -> HttpResponse:
    """Отображает список постов указанной категории."""
    requested_category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )
    post_list = requested_category.posts.all()
    context = {
        'category': requested_category,
        'post_list': post_list
    }
    return render(request, 'blog/category.html', context)
