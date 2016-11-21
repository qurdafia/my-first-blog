#from django.contrib.auth.models import User
from django import forms
from .models import Post, Comment
from django.contrib.auth import get_user_model
User = get_user_model()


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('image', 'title', 'text', )

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)

class UserRegistrationForm(forms.ModelForm):
    email = forms.EmailField(label='Email address')
    email2 = forms.EmailField(label='Confirm email')
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = (
            'email',
            'email2',
            'username',
            'password',
        )

    def clean_email2(self):
        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')
        if email != email2:
            raise forms.ValidationError('Emails must match.')
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError('Email has already been taken.')
        return email

