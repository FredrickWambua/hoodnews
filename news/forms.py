from django.contrib.auth import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import *
from django import forms
from django.forms import fields


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email',)


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30, required=False)
    email = forms.EmailField(max_length=255, help_text='Required. Inform a valid email address.')

    class Meta:
        model = CustomUser
        fields = ('username','email', 'password1', 'password2')
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model  =CustomUser
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user', 'neighborhood')

class NeighborhoodForm(forms.ModelForm):
    class Meta:
        model = Neighborhood
        exclude = ('admin', )

class NewsPostForm(forms.ModelForm):
    class Meta:
        model = NewsPost
        exclude = ('user', 'hood')

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ('user', 'neighborhood')