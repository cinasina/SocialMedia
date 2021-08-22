from django.shortcuts import render
from Post.models import Post


def home(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'home/home.html', context=context)
