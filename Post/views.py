from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Post
from Comments.models import Comment
from .forms import AddPostForm, EditPostForm
from Comments.forms import AddCommentForm, AddReplyForm
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required
from Like.models import Like


@login_required
def post_details(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = Comment.objects.filter(post=post, is_reply=False)
    liked = Like.objects.filter(user=request.user, post=post, is_liked=True)
    reply = AddReplyForm()
    if request.method == 'POST':
        form = AddCommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.user = request.user
            new_comment.post = post
            new_comment.save()
            messages.success(request, 'Added The Comment', 'success')
    else:
        form = AddCommentForm
    return render(request, 'post/details.html', {'post': post, 'comments': comments,
                                                 'form': form, 'reply': reply, 'liked': liked,
                                                 })


@login_required
def add_post(request, profile_id):
    if request.user.id == profile_id:
        if request.method == 'POST':
            form = AddPostForm(request.POST)
            if form.is_valid():
                new_post = form.save(commit=False)
                new_post.user = request.user
                new_post.slug = slugify(form.cleaned_data['text'][:15])
                new_post.save()
                messages.success(request, 'Post Is Added', 'success')
                return redirect('accounts:profile:user_profile', profile_id)


@login_required
def edit_post(request, profile_id, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.user.id == profile_id:
        if request.method == 'POST':
            form = EditPostForm(request.POST, instance=post)
            if form.is_valid():
                ed_post = form.save(commit=False)
                ed_post.user = request.user
                ed_post.slug = slugify(form.cleaned_data['text'][:15])
                ed_post.save()
                messages.success(request, 'Post Is Changed', 'success')
                return redirect('accounts:profile:user_profile', profile_id)
        else:
            form = EditPostForm(instance=post)
        return render(request, 'post/edit_post.html', {'form': form})


@login_required
def delete_post(request, profile_id, post_id):
    if request.user.id == profile_id:
        Post.objects.filter(pk=post_id).delete()
        messages.success(request, 'Your Post Is Deleted Successfully', 'success')
        return redirect('accounts:profile:user_profile', profile_id)
    else:
        return redirect('home:home')


