from django.shortcuts import render, redirect, get_object_or_404
from .models import Follow
from django.contrib.auth.models import User
from Profile.models import Profile


def follow(request, user_id, profile_id):
    follower = get_object_or_404(User, pk=user_id)
    following = get_object_or_404(Profile, pk=profile_id)
    relation = Follow(follower=follower, following=following, is_following=True)
    relation.save()
    following.follower.add(follower.pk)
    follower.profile.following.add(following.pk)
    return redirect('accounts:profile:user_profile', profile_id)


def unfollow(request, user_id, profile_id):
    follower = get_object_or_404(User, pk=user_id)
    following = get_object_or_404(Profile, pk=profile_id)
    relation = Follow.objects.filter(follower=follower, following=following, is_following=True)
    relation.delete()
    following.follower.remove(follower.pk)
    follower.profile.following.remove(following.pk)
    return redirect('accounts:profile:user_profile', profile_id)
