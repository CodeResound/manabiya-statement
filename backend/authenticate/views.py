import datetime
from typing import Any, Optional, Set, Tuple, TypeVar
from django.db import transaction

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser
from rest_framework.views import APIView

from manabiyacentral.middlewares.parsers import RequestParser
from manabiyacentral.utility.helpers import Argon2
from manabiyacentral.handlers.errorHandler.api_exceptions import LoginException, AuthenticationError, TokenBackendError

from .backend import TokenBackend

from .models import Users

from .serializers import (
    LoginSerializer,
    UsersSerializer,
)

from .backend import TokenBackend

class UsersView(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    parser_classes = [MultiPartParser, RequestParser]


class Login(APIView):
    authentication_classes = []
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
        
        user.last_login = datetime.datetime.now(datetime.timezone.utc)
        user.login_attempts = 0
        user.session_at = datetime.datetime.now(datetime.timezone.utc)

        token = TokenBackend()
        payload = {
            'user_id': str(user.id),
            'name' : user.name
        }

        access_token = token.encode(payload,'access')
        refresh_token = token.encode(payload,'refresh')

        response = Response({'access_token':access_token,'message':'Login Successful'}, status=status.HTTP_200_OK)
        response.set_cookie(
        key='refresh_token',
        value=refresh_token,
        httponly=True,
        secure=False, 
        samesite='None'  
    )
        return response


class RefreshToken(APIView):
    authentication_classes= []
    def post(self, request):
        raw_refresh_token = self.get_refresh_token(request)
        token_backend = TokenBackend()
        refresh_payload = token_backend.decode(token=raw_refresh_token)
        try:
            payload = {
                'user_id' : str(refresh_payload.get('user_id')),
                'name' : refresh_payload.get('name')
            }

            new_access_token = token_backend.encode(payload, 'access')

            response = Response({'message':'Token Refreshed'}, status=status.HTTP_200_OK)
            response['XAuthorization'] = new_access_token
            return response
        except Exception as e:
            raise TokenBackendError('Unable to Refresh Access Token. Please Proceed to Login')


    def get_refresh_token(self, request) -> Optional[str]:
        refresh_token = request.COOKIES.get('refresh_token')
        if refresh_token is None:
            raise AuthenticationError('Unable to Process Your Request. Refresh Token Not Found')
        return refresh_token

        
class Logout(APIView):
    def post(self, request):
        response = Response({'message':'You have been Logged Out.'}, status=status.HTTP_204_NO_CONTENT)
        response.delete_cookie('refresh_token') 