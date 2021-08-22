from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Profile
from .forms import EditProfileForm
from Post.forms import AddPostForm
from Post.models import Post
from django.contrib.auth.decorators import login_required
from Follow.models import Follow


@login_required
def user_profile(request, profile_id):
    profile = get_object_or_404(Profile, pk=profile_id)
    posts = Post.objects.filter(user=request.user)
    relation = Follow.objects.filter(follower=request.user, following=profile, is_following=True)
    form = AddPostForm()
    context = {'profile': profile, 'form': form, 'posts': posts, 'relation': relation}
    return render(request, 'profile/profile.html', context=context)


@login_required
def edit_profile(request, profile_id):
    if request.user.id == profile_id:
        user_edit = get_object_or_404(Profile, pk=profile_id)
        if request.method == 'POST':
            form = EditProfileForm(request.POST, instance=user_edit)
            if form.is_valid():
                form.save()
                user_edit.user.username = form.cleaned_data['username']
                user_edit.user.first_name = form.cleaned_data['first_name']
                user_edit.user.last_name = form.cleaned_data['last_name']
                user_edit.user.email = form.cleaned_data['email']
                user_edit.user.save()
                messages.success(request, 'Your Profile Edited Successfully', 'success')
                return redirect('accounts:profile:user_profile', profile_id)
        else:
            form = EditProfileForm(instance=user_edit, initial={
                'email': user_edit.user.email,
                'first_name': user_edit.user.first_name,
                'last_name': user_edit.user.last_name,
                'username': user_edit.user.username,
            })
        return render(request, 'profile/edit_profile.html', {'form': form})
