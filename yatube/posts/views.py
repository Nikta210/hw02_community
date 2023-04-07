from django.shortcuts import get_object_or_404, render, redirect
from django.core.paginator import Paginator
from .models import Group, Post
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from .form import PostForm
from datetime import timezone

NUM_OUT_POSTS = 10
User = get_user_model()


def index(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, NUM_OUT_POSTS)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'posts/index.html', context)

def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()
    paginator = Paginator(posts, NUM_OUT_POSTS)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'group': group,
        'page_obj': page_obj,
    }
    return render(request, 'posts/group_list.html', context)

def profile(request, username):
    user_obj = get_object_or_404(User, username=username)
    posts = user_obj.posts.all()
    paginator = Paginator(posts, NUM_OUT_POSTS)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'user_obj': user_obj,
        'page_obj': page_obj,
    }
    return render(request, 'posts/profile.html', context)

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {
        'post': post,
    }
    return render(request, 'posts/post_detail.html', context)

@login_required
def post_create(request):
    template = 'posts/create_post.html'
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect ('')
    form = PostForm()
    return render(request, template, {'form':form})



    