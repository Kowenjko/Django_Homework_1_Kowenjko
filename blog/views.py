from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from django.utils import timezone
from blog import *
from .models import Post

# get method


def post_list(request):
    posts = Post.objects.filter(
        publish_date__lte=timezone.now()).order_by('publish_date')
    # posts = Post.objects.all()
    return render(request, 'blog/post_lists.html', {'posts': posts})
