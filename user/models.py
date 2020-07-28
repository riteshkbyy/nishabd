from django.db import models

# Create your models here.
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.conf import settings
import datetime

class UserProfile(models.Model):

    GENDER_CHOICES = (
        ('m', 'Male'),
        ('f', 'Female'),
        ('u', 'Prefer not to say')
    )
    MARITAL_STATUS_CHOICES = (
        ('m', 'Married'),
        ('u', 'Unmarried'),
        ('d', 'Divorced'),
        ('w', 'Widowed'),
    )
    name = models.CharField(max_length=100, verbose_name="Name: ", blank=True)
    profile_picture = models.ImageField(verbose_name="Profile Picture: ",  blank = True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name="Gender", blank=True)
    about = models.TextField(max_length=300, verbose_name="About me: ", blank = True)
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Created Date", null=True)


    def save(self, *args, **kwargs):
        return super(UserProfile, self).save(*args, **kwargs) 