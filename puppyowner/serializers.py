from rest_framework import serializers
from .models import EmdeeBlog, PupOwnerRegistration
from .models import Puppy
from .models import BookedApps
from .models import EmdeeContact

class PupOwnerRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PupOwnerRegistration
        fields = ['name', 'last_name', 'email', 'street_address', 'city', 'state', 'zip_code', 'rating', 'user_id']
class contactSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmdeeContact
        fields = '__all__'

class EmdeeBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmdeeBlog
        fields = '__all__'
        
class PuppySerializer(serializers.ModelSerializer):
    class Meta:
        model = Puppy
        fields = ['name', 'breed', 'age', 'vaccinated', 'description', 'price', 'user']

class BookedAppsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookedApps
        fields = ['name', 'last_name', 'user_name', 'time', 'address', 'user_id']
