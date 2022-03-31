from rest_framework import serializers
from .models import userAbstract

class authSerializer(serializers.ModelSerializer):
    class Meta:
        model = userAbstract
        fields = ['firstname', 'lastname', 'email', 'phonenumber', 'password']
        extra_kwargs ={
            'password': {'write_only': True}
        }
    def create(self, validate_date):
        password = validate_date.pop('password', None)
        instance = self.Meta.model(**validate_date)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
