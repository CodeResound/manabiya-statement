import re
from rest_framework import serializers
from manabiyacentral.utility.helpers import Argon2

from .models import Users

class UsersSerializer(serializers.ModelSerializer):
    
    def validate_password(self, value):
        regex = r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[\W_]).{8,}$"
        if re.match(regex, value):
            hasher = Argon2()
            hashed_password = hasher.hash_password(password=value)
            return hashed_password
        return serializers.ValidationError({'password':'Password Must Be of 1 Letter, 1 Number and 1 Special Characters'})
    
    class Meta:
        model = Users
        fields = '__all__'
    


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    def validate_password(self, value):
        regex = r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[\W_]).{8,}$"
        if re.match(regex, value):
            return value
        return serializers.ValidationError({'password':'Password Must Be of 1 Letter, 1 Number and 1 Special Characters'})
