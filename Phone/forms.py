from django import forms


class LoginPhoneForm(forms.Form):
    phone = forms.IntegerField()


class VerifyPhoneForm(forms.Form):
    code = forms.IntegerField()
