from django.contrib import admin
from .models import *


class puppyClass(admin.ModelAdmin):
    list_display = ['id', 'name']

class emdeeBlogClass(admin.ModelAdmin):
    list_display = ['id','titleTxt', 'perNight', 'reviews', 'rating']

class emdeeContactClass(admin.ModelAdmin):
    list_display = ['id','feedbacktype', 'fullname', 'email', 'description']


# admin.site.register(PupOwnerRegistration)
# admin.site.register(Puppy, puppyClass)
# admin.site.register(BookedApps)
admin.site.register(EmdeeContact, emdeeContactClass)
admin.site.register(EmdeeBlog, emdeeBlogClass)
