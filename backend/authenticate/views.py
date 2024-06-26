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

