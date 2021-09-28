from django.shortcuts import render
from .signals import *
from django.shortcuts import get_object_or_404, render,redirect, resolve_url
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib import messages
from news.forms import *







# Create your views here.
def home(request):
    posts = Neighborhood.objects.all().order_by('-pk')
    return render(request, 'news/index.html',{'posts': posts})

def signup(request):
    if request.method == 'POST':     
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, f'Hi {username} Your account was created successfully. ')
            return redirect('home')
    else:
        form = SignUpForm

    return render(request, 'registration/signup.html', {'form':form,'registered': False } )

@login_required
def profile(request):
    title = 'Your Profile Information'
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f'Your profile has been updated successfully.')
            return redirect('home')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
        context = {
            'title': title,
            'user_form': user_form,
            'profile_form': profile_form,
        }
        return render(request, 'news/profile.html', context)

@login_required
def ProfileDetail(request):
    current_user = request.user
    return render(request, 'news/profile_details.html', {'current_user': current_user})