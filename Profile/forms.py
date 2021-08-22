from django import forms
from .models import User, Profile


class EditProfileForm(forms.ModelForm):
    username = forms.CharField(max_length=15, min_length=4)
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=30)

    class Meta:
        model = Profile
        fields = ('bio', 'phone',)
