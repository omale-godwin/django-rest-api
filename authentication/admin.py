from django.contrib import admin
from.models import userAbstract

# Register your models here.

class userClass(admin.ModelAdmin):
    list_display = ['firstname', 'lastname', 'email', 'phonenumber',]
    list_filter = ['firstname', 'phonenumber','email']
 
    
admin.site.register(userAbstract, userClass)