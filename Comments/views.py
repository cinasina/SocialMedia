from django.shortcuts import render, redirect, get_object_or_404
from .forms import AddReplyForm
from .models import Comment
from Post.models import Post
from django.contrib import messages


def add_reply(request, post_id, cm_id):
    post = get_object_or_404(Post, pk=post_id)
    comment = get_object_or_404(Comment, pk=cm_id)
    if request.method == 'POST':
        forms = AddReplyForm(request.POST)
        if forms.is_valid():
            reply = forms.save(commit=False)
            reply.user = request.user
            reply.post = post
            reply.self_cm = comment
            reply.is_reply = True
            reply.save()
            messages.success(request, 'Your Reply Is Added Now', 'success')
    return redirect('post:details', post.slug)
