from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login
from .forms import LoginPhoneForm, VerifyPhoneForm
from Profile.models import Profile
from django.contrib import messages
from random import randint


def login_phone(request):
    if request.method == 'POST':
        form = LoginPhoneForm(request.POST)
        if form.is_valid():
            phone = 0 + form.cleaned_data['phone']
            find_phone = Profile.objects.filter(phone=phone)
            if not find_phone.exists():
                messages.error(request, "This Phone Number Doesn't Exist", extra_tags='warning')
            else:
                random_number = randint(1000, 9999)
                print(random_number)
                request.session['phone'] = phone
                request.session['random_number'] = random_number
                # Enter The Settings Of OPT
                return redirect('accounts:phone_login:verify_phone')
    else:
        form = LoginPhoneForm()
    return render(request, 'phone/login_phone.html', {'form': form})


def verify_phone(request):
    if request.method == 'POST':
        form = VerifyPhoneForm(request.POST)
        if form.is_valid():
            phone = request.session['phone']
            random_number = request.session['random_number']
            if form.cleaned_data['code'] == random_number:
                phone_profile = get_object_or_404(Profile, phone=phone)
                user = get_object_or_404(User, profile__id=phone_profile.id)
                login(request, user=user, backend='django.contrib.auth.backends.ModelBackend')
                messages.success(request, 'You Are Login Now', extra_tags='success')
                return redirect('home:home')
            else:
                messages.error(request, 'Your Code Is Wrong', extra_tags='warning')
    else:
        form = VerifyPhoneForm()
    return render(request, 'phone/login_phone.html', {'form': form})

