from rest_framework import serializers
from .models import UserRegisterModel

class UserRegistrationSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserRegisterModel
        fields = ['first_name','last_name','profile_pic','date_of_birth','city','country']


