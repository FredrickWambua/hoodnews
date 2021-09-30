from django.urls import include, path
from . import views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('myprofile/', views.ProfileDetail, name='myprofile'),
    path('hoods/', views.TheHood, name='hood'),
    path('createhood/', views.CreateHood, name='createhood'),
    path('singlehood/', views.SingleHood, name='singlehood'),
    path('joinhood/', views.JoinHood, name='joinhood'),
    path('leavehood/', views.LeaveHood, name='leavehood'),
    path('post/<int:id>', views.CreatePost, name='post'),
    path('occupants/<int:id>', views.Occupants, name='occupants'),
    path('search/', views.Search, name= 'search'),



]