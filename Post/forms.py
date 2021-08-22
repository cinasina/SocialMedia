from django import forms
from .models import Post


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('text',)
        labels = {
            'text': '',
        }
        widgets = {
            'text': forms.TextInput(
                attrs={"class": "form-control", "id": "message", "rows": "3", "placeholder": "What Are You Thinking?"}
            )}


class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('text',)
        labels = {
            'text': '',
        }
        widgets = {
            'text': forms.TextInput(
                attrs={"class": "form-control", "id": "message", "rows": "3", }
            )}


