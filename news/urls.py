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
    path('singlehood/<hood_id>', views.SingleHood, name='singlehood'),
    path('joinhood/<int:id>', views.JoinHood, name='joinhood'),
    path('leavehood/<int:id>', views.LeaveHood, name='leavehood'),
    path('post/<hood_id>', views.CreatePost, name='post'),
    path('occupants/<int:id>', views.Occupants, name='occupants'),
    path('search/', views.Search, name= 'search'),



]