from django.shortcuts import get_object_or_404, render

from .models import Group, Post


# Create your views here.
def index(request):
    posts = Post.objects.order_by('-pub_date')[:10]
    return render(request, 'index.html', {'posts': posts})


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:12]
    return render(request, 'group.html', {'group': group, 'posts': posts})