import datetime

from django.db import transaction

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser
from rest_framework.views import APIView

from manabiyacentral.middlewares.parsers import RequestParser
from manabiyacentral.utility.helpers import Argon2
from manabiyacentral.handlers.errorHandler.api_exceptions import LoginException

from .models import Users

from .serializers import (
    LoginSerializer,
    UsersSerializer
)

class UsersView(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    parser_classes = [MultiPartParser, RequestParser]


class Login(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']
        try:
            user = Users.objects.get(username=username)
        except Users.DoesNotExist:
            raise LoginException('Unable To Login. Invalid Credentials.')
        
        if user.status is False:
            raise LoginException('For Security Purpose, Your Account is Currently Suspended. Please Contact Support')
        
        if user.login_attempts > 4:
            login_attempts = user.login_attempts
            last_login_datetime = user.cooldown_time
            time_difference = datetime.datetime.now(datetime.timezone.utc) - last_login_datetime
            cooldown_count = (login_attempts // 5) * 5
            if time_difference <= datetime.timedelta(minutes=cooldown_count):
                raise LoginException(f'For Security Purpose, Your Account is on Cooldown. Please Try Again After {cooldown_count} minutes.')
            else:
                pass
        
        argon2_instance = Argon2()
        if argon2_instance.verify_password(stored_hash=user.password, password=password) is False:
            user.last_login = datetime.datetime.now(datetime.timezone.utc)
            login_attempts = user.login_attempts
            user.login_attempts = user.login_attempts + 1

            if (login_attempts + 1) == 5:
                user.cooldown_time = datetime.datetime.now(datetime.timezone.utc)
            
            if (login_attempts + 1) > 9:
                user.status = False
            
            user.save()
            raise LoginException('Unable to Login. Invalid Credentials.')
        

