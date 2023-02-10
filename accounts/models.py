from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


# Create your models here.
# User accounts Manager

class CustomUserManager(BaseUserManager):
    def create_user(self, email, last_name, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        if not last_name:
            raise ValueError('User must provide lastname')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        last_name = last_name,
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, last_name, password, **extra_fields):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(email, last_name, password=password, **extra_fields)
        last_name = last_name,
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user


class BaseUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    last_name = models.CharField(max_length=255)
    # required Fields
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    # I set to False to so i can verified the mail of the user ie is_active is always True when am not verifing a user
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    # login
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['last_name']
    #  u will always need to end the class with() or natural key error awaits
    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True


class EKKPastor(BaseUser):
    first_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=50)

    def get_full_name(self):
        return self.first_name + " " + self.last_name


class Busscell(BaseUser):
    first_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=50)

    def get_full_name(self):
        return self.first_name + " " + self.last_name
