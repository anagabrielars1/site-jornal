from django.shortcust import render
from .models import post

def post_list(request):
    posts = post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

