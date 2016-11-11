from django.contrib.auth.models import User

from django import forms

from .models import Post, Comment

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('image', 'title', 'text', )

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)
