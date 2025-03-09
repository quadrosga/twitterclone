from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Tweet, Profile, Follow

admin.site.register(Tweet)
admin.site.register(Profile)
admin.site.register(Follow)