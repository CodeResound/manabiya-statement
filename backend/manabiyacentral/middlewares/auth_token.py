from typing import Any, Optional, Set, Tuple, TypeVar

from django.utils.deprecation import MiddlewareMixin
from rest_framework.response import Response

from authenticate.models import Users
from rest_framework import HTTP_HEADER_ENCODING, authentication
from rest_framework.request import Request

from authenticate.backend import TokenBackend
from manabiyacentral.handlers.errorHandler.api_exceptions import InvalidToken, TokenBackendError, AuthenticationError, NotFound

from authenticate.utils import (
    aware_utcnow,
    datetime_to_epoch
)

AUTH_HEADER_TYPES = ("Kilimanjaro",)

AUTH_HEADER_TYPE_BYTES : Set[bytes] = {
    h.encode(HTTP_HEADER_ENCODING) for h in AUTH_HEADER_TYPES
}


class JWTAuthentication(authentication.BaseAuthentication):
    www_authenticate_realm = 'api'
    media_type = 'application/json'

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)  
        self.user_model = Users
        self.token_backend = TokenBackend()
             

    def authenticate(self, request:Request)-> Optional[Tuple[Users, str]]:
        header = self.get_header(request)

        if header is None:
            raise AuthenticationError('Unable to Process Your Request. Error: Missing Authentication Headers.')

        raw_token = self.get_raw_token(header)
        if raw_token is None:
            raise AuthenticationError('Unable to Process Your Request. Error: Invalid Authorization Header')
        
        decoded_token = raw_token.decode('utf-8')
        
        self.payload = self.token_backend.decode(token=raw_token)

        user_id = self.payload.get('user_id')
        if not user_id:
            raise InvalidToken('Unable to Process Your Request. Error: Contaminated Token Structure. Id Parameters Missing.')
        
        try:
            user = self.user_model.objects.get(id=user_id)
        except self.user_model.DoesNotExist:
            raise NotFound()
        
        return user, decoded_token

        
    def authenticate_header(self, request:Request)-> str:
        return '{} realm="{}"'.format(
            AUTH_HEADER_TYPES[0],
            self.www_authenticate_realm
        )
    

    def get_header(self, request:Request)->bytes:
        #Extracts the header from the request
        header = request.headers.get('Authorization')
        if isinstance(header, str):
            header = header.encode(HTTP_HEADER_ENCODING)
        return header

    
    def get_raw_token(self, header: bytes)-> Optional[bytes]:
        parts = header.split()
        if len(parts) == 0:
            raise AuthenticationError('Invalid Header. Authorization Header Must Contain Two Space Delimited Values')
        if parts[0] not in AUTH_HEADER_TYPE_BYTES:
            raise AuthenticationError('Invalid Header. Authorization Header Not Following Specified Format.')
        if len(parts) !=2:
            raise AuthenticationError('Invalid Header. Authorization Header Must Contain Two Space Delimited Values')
        return parts[1]    

        

        
        

    
    



                      
