from django.contrib import admin

# Register your models here.
from .models import Profile,ProfileStatus


admin.site.register(Profile)
admin.site.register(ProfileStatus)
