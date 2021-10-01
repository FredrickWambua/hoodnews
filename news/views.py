from django.contrib.auth.backends import RemoteUserBackend
from django.shortcuts import render
from .signals import *
from django.shortcuts import get_object_or_404, render,redirect, resolve_url
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib import messages
from news.forms import *
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q









# Create your views here.
def home(request):
    posts = Neighborhood.objects.all().order_by('-pk')
    return render(request, 'news/index.html',{'posts': posts})

csrf_exempt
def signup(request):
    if request.method == 'POST':     
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            messages.success(request, f'Hi {username} Your account was created successfully. ')
            return redirect('login')
    else:
        form = SignUpForm

    return render(request, 'registration/signup.html', {'form':form,'registered': False } )

csrf_exempt
@login_required
def profile(request):
    title = 'Your Profile Information'
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('hood')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
        context = {
            'title': title,
            'user_form': user_form,
            'profile_form': profile_form,
        }
        return render(request, 'news/profile.html', context)


csrf_exempt
@login_required
def ProfileDetail(request):
    current_user = request.user
    return render(request, 'news/profile_details.html', {'current_user': current_user})

def TheHood(request):
    hoods = Neighborhood.objects.all()
    return render(request, 'news/hoods.html', {'hoods': hoods})

def CreateHood(request):
    if request.method == 'POST':
        form = NeighborhoodForm(request.POST)
        if form.is_valid():
            hood = form.save(commit=False)
            hood.admin = request.user.profile
            hood.save()
            return redirect('hood')
    else:
        form = NeighborhoodForm()
    return render(request, 'news/createhood.html', {'form': form})

def SingleHood(request, hood_id):
    hood = Neighborhood.objects.get(id=hood_id)
    occupants = Profile.objects.filter(neighborhood=hood)
    business = Business.objects.filter(neighborhood=hood)
    posts = NewsPost.objects.filter(hood=hood)
    posts = posts[::-1]
    if request.method == 'POST':
        form = BusinessForm(request.POST)
        if form.is_valid():
            b_form = form.save(commit=False)
            b_form.neighbourhood = hood
            b_form.user = request.user.profile
            b_form.save()
            return redirect('news/singlehood', hood.id)
    else:
        form = BusinessForm()
    context = {
        'hood': hood,
        'business': business,
        'form': form,
        'posts': posts,
        'occupants': occupants
    }
    return render(request, 'news/singlehood.html', context)   

def Occupants(request, hood_id):
    hood = Neighborhood.objects.get(id=hood_id)
    occupants = Profile.objects.filter(neighborhood=hood)
    return render(request, 'news/occupants.html', {'occupants': occupants})


def JoinHood(request, id):
    hood = get_object_or_404(Neighborhood, id=id)
    request.user.profile.neighborhood=hood
    request.user.profile.save()
    return redirect('hood')

def LeaveHood(request, id):
    hood = get_object_or_404(Neighborhood, id=id)
    request.user.profile.neighborhood = None
    request.user.profile.save()
    return redirect('hood')

def CreatePost(request, hood_id):
    hood = Neighborhood.objects.get(id=hood_id)
    if request.method == 'POST':
        form = NewsPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.hood = hood
            post.user = request.user.profile
            post.save()
            return redirect('singlehood', hood.id)
    else:
        form = NewsPostForm()
    return render(request, 'news/post.html', {'form': form})


@login_required
def Search(request):
    if request.method=='GET':
        result = request.GET.get('q')
        if result:
            display = Business.objects.filter(Q(name__icontains = result))
            return render(request, 'news/search.html',  {'display': display})
            
        else:
            message = "No information found from your search. Try to refine your search term"
            return render(request, 'news/search.html',{"message":message})