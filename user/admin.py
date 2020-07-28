from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import UserProfile

# Register your models here.
@admin.register(UserProfile)
class UserProfile(admin.ModelAdmin):

    list_display = ["profile_picture","user","gender", "about"]

    list_display_links = ["user","about"]

    search_fields = ["User", "about"]

    list_filter = ["created_date"]

    class Meta:
        model = UserProfile

