from django.shortcuts import render, get_object_or_404
from .models import Post, Group
from yatube.settings import COUNT_POSTS
from django.core.paginator import Paginator
from django.views.generic.base import TemplateView

def index(request):
    posts = Post.objects.select_related('author', 'group')
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'posts': posts,
        'page_obj': page_obj,
    }
    return render(request, 'posts/index.html', context)

def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.select_related('author', 'group')[:COUNT_POSTS]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)

def profile(request, username):
    context = {
    }
    return render(request, 'posts/profile.html', context)

def post_detail(request, post_id):
    context = {
    }
    return render(request, 'posts/post_detail.html', context)

def post_create(request):
    form = PostForm()
    context = {
        'form': form,
    }
    return render(request, 'posts/create_post.html', context)

def post_edit(request):
    form = PostForm()
    context = {
        'form': form,
    }
    return render(request, 'posts/create_post.html', context)