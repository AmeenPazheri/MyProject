from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin

from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):

        if not email:
            raise ValueError('User must have a Email')
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.user_type='U'
        user.save(using=self._db)
        if user:
            return user

    def create_admin_user(self, email, password=None, **extra_fields):

        if not email:
            raise ValueError('User must have a Email')
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.user_type='A'
        user.save(using=self._db)
        if user:
            return user

    def create_superuser(self, email, password):

        user = self.model(email=email)
        user.set_password(password)
        user.save(using=self.db)
        user.is_staff = True
        user.is_superuser = True
        user.user_type='S'
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    USER_TYPE_CHOICES = [
        ('S', 'Super User'),
        ('A', 'Admin'),
        ('U', 'User'),
    ]
    email = models.EmailField(max_length=225, unique=True)
    user_type= models.CharField(max_length=1, choices=USER_TYPE_CHOICES)
    is_staff = models.BooleanField(default=False)
    objects=UserManager()

    USERNAME_FIELD='email'

class Vehicle(models.Model):
    VEHICLE_TYPE_CHOICES = [
        ('2W', 'Two Wheeler'),
        ('3W', 'Three Wheeler'),
        ('4W', 'Four Wheeler'),
    ]
    vehicle_number = models.CharField(max_length=20)
    vehicle_type = models.CharField(max_length=2, choices=VEHICLE_TYPE_CHOICES)
    vehicle_model = models.CharField(max_length=100)
    vehicle_description = models.TextField()

    def __str__(self):
        return self.vehicle_number
