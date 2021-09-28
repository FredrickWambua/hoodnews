from django.contrib.auth import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import *
from django import forms
from django.forms import fields


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
