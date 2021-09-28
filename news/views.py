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


