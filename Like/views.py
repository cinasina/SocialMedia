from django.shortcuts import get_object_or_404, redirect
from .models import Like
from Post.models import Post
from django.contrib.auth.decorators import login_required


@login_required
def post_like(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    like = Like(user=request.user, post=post, is_liked=True)
    like.save()
    return redirect('post:details', post.slug)


@login_required
def post_unlike(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    like = Like.objects.get(user=request.user, post=post, is_liked=True)
    like.delete()
    return redirect('post:details', post.slug)





