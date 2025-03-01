from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, email, name, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, **extra_fields)
        user.set_password(password)  # Hashes the password
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, name, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    newsletter = models.BooleanField(default=False)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.email


class PartnerApplication(models.Model):
    PARTNER_TYPES = [
        ('BDA', 'BDA Partner'),
        ('Store', 'Store Partner'),
        ('Studio', 'Studio Partner'),
        ('Delivery', 'Delivery Partner')
    ]
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    message = models.TextField(blank=True, null=True)
    partner_type = models.CharField(
        max_length=20, choices=PARTNER_TYPES, default='BDA'
    )
    created_at = models.DateTimeField(auto_now_add=True)

class HelpRequest(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    contact = models.CharField(max_length=15)
    email = models.EmailField()
    query = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
