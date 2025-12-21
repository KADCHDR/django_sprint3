from django.shortcuts import render, get_object_or_404
from django.utils.timezone import now
from .models import Post, Category

# 👇 временные посты, переделанные под тебя


def main_feed(request):
    posts = Post.objects.filter(
        pub_date__lte=now(),
        is_published=True,
        category__is_published=True
    ).order_by('-pub_date')[:5]
    return render(request, 'blog/index.html', {'post_list': posts})

def entry_view(request, entry_id):
    post = get_object_or_404(Post, pk=entry_id,
                             is_published=True,
                             pub_date__lte=now(),
                             category__is_published=True)
    return render(request, 'blog/detail.html', {'post': post})

def category_view(request, cat_slug):
    category = get_object_or_404(Category, slug=cat_slug, is_published=True)
    posts = Post.objects.filter(
        category=category,
        pub_date__lte=now(),
        is_published=True
    ).order_by('-pub_date')
    return render(request, 'blog/category.html', {'post_list': posts, 'category': category})
