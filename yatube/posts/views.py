from django.shortcuts import render, get_object_or_404
from .models import Post, Group, User
from yatube.settings import COUNT_POSTS
from django.core.paginator import Paginator
from posts.forms import PostForm

def index(request):
    posts = Post.objects.select_related('author', 'group')
    paginator = Paginator(posts, COUNT_POSTS)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'posts': posts,
        'page_obj': page_obj,
    }
    return render(request, 'posts/index.html', context)

def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.select_related('author', 'group')
    paginator = Paginator(posts, COUNT_POSTS)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'group': group,
        'posts': posts,
        'page_obj': page_obj,
    }
    return render(request, 'posts/group_list.html', context)

def profile(request, username):
    author = get_object_or_404(User, username=username)
    posts = Post.objects.filter(author=author) 
    paginator = Paginator(posts, COUNT_POSTS)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'author': author,
        'page_obj': page_obj,
    }
    return render(request, 'posts/profile.html', context)

def post_detail(request, post_id):
    posts = get_object_or_404(Post, pk=post_id)
    context = {
        'posts': posts,
    }
    return render(request, 'posts/post_detail.html', context)

def post_create(request):
    form = PostForm()
    context = {
        'form': form,
    }
    return render(request, 'posts/create_post.html', context)

def post_edit(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    form = PostForm()
    context = {
        'form': form,
        'post': post,
    }
    return render(request, 'posts/create_post.html', context)