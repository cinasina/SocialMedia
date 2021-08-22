from django import forms


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=20, min_length=4, label='',
                               widget=forms.TextInput(
                                   attrs={'class': "un", "type": "text", "align": "center", "placeholder": "Username"}))
    password = forms.CharField(max_length=20, min_length=4, label='',
                               widget=forms.PasswordInput(attrs={"class": "pass", "type": "password", "align": "center",
                                                                 "placeholder": "Password"}))


class UserRegisterForm(forms.Form):
    username = forms.CharField(max_length=20, min_length=4, label='',
                               widget=forms.TextInput(
                                   attrs={'class': "un", "type": "text", "align": "center",
                                          "placeholder": "Username"}))
    email = forms.CharField(max_length=20, min_length=4, label='',
                            widget=forms.EmailInput(
                                attrs={'class': "un", "type": "text", "align": "center",
                                       "placeholder": "Email"}))
    password = forms.CharField(max_length=20, min_length=8, label='',
                               widget=forms.PasswordInput(
                                   attrs={'class': "pass", "type": "password", "align": "center",
                                          "placeholder": "Password"}))
