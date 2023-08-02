from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import  User, Post


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password1', 'password2']


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body']


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email']
        