from django.shortcuts import get_object_or_404, render

from .models import Group, Post


def index(request):
    num_out_posts = 10
    posts = Post.objects.order_by('-pub_date')[:num_out_posts]
    title = 'Последние обновления на сайте'
    context = {
        'posts': posts,
        'title': title,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    num_out_posts = 10
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:num_out_posts]
    title = f'Записи сообщества {slug}'
    context = {
        'group': group,
        'posts': posts,
        'title': title,
    }
    return render(request, 'posts/group_list.html', context)
