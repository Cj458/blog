from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

import requests

from .models import Post, User
from .forms import PostForm, UserForm, MyUserCreationForm


def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        # email = request.POST.get('email').lower()
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username OR password does not exit')

    context = {'page': page}
    return render(request, 'base/login-register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home')


def registerPage(request):
    form = MyUserCreationForm()

    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occurred during registration')

    return render(request, 'base/login-register.html', {'form': form})


def home(request):
    all_user_api_endpoint = 'http://127.0.0.1:8000/api/myusers/'
    response_users = requests.get(all_user_api_endpoint)

    users = response_users.json()
   
    context = {'users': users}
    return render(request, 'base/home.html', context)


@login_required(login_url='login')
def updateUser(request):
    user = request.user
    form = UserForm(instance=user)

    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user-profile', pk=user.id)

    return render(request, 'base/update-user.html', {'form': form})


def topicsPage(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    posts = Post.objects.filter(name__icontains=q)
    return render(request, 'base/posts.html', {'topics': posts})

def userProfile(request, pk):
    user = User.objects.get(id=pk)
    
    posts = user.posts.all()

    context = {'user': user, 'posts': posts}
    return render(request, 'base/profile.html', context)


def postPage(request):
    pass

@login_required(login_url='login')
def view_user_posts(request, user_id):

    user = get_object_or_404(User, pk=user_id)
    posts = Post.objects.filter(user=user)

    context = {
        'user': user,
        'posts': posts,
    }

    return render(request, 'base/view-user-posts.html', context)


@login_required(login_url='login')
def edit_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if 'delete' in request.POST:
            post.delete()
            return redirect('view_user_posts', user_id=post.user.id)
        elif form.is_valid():
            form.save()
            return redirect('view_user_posts', user_id=post.user.id)
    else:
        form = PostForm(instance=post)

    return render(request, 'base/edit-post.html', {'form': form, 'post': post})


@login_required(login_url='login')
def create_post_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            
            new_post = form.save(commit=False)
            new_post.user = request.user
            new_post.save()
            return redirect('post_detail', pk=new_post.pk)

    else:
        form = PostForm()

    return render(request, 'base/create-post.html', {'form': form})

def post_detail_view(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'base/post-detail.html', {'post': post})


