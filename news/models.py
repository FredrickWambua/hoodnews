from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.db import models
from cloudinary.models import CloudinaryField
from PIL import Image

# Create your models here.
class CustomUserManager(BaseUserManager):
    '''
    Custom user manager where email is the unique identifiers
    for authentication instead of username
    '''
    def create_user(self, email, password, **kwargs):
        '''
        Create and save a User with the given email and password.
        '''
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password =(password)
        user.save()
        return user
    def create_superuser(self, email, password, **kwargs):
        '''
        Create and save a superuser with the given email and password.
        '''
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        kwargs.setdefault('is_active', True)

        if kwargs.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True'))
        if kwargs.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True'))
        return self.create_user(email, password, **kwargs)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255)
    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()


    def __str__(self):
        return self.email