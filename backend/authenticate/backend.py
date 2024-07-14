import os
import datetime

from datetime import timedelta
from collections.abc import Iterable

import jwt
from jwt import InvalidTokenError

from typing import Optional, Dict, Any
from django.conf import settings

from manabiyacentral.handlers.errorHandler.api_exceptions import TokenBackendError


class TokenBackend:
    def __init__(self) -> None:
        self.algorithm = os.getenv('TOKEN_ALGORITHM')
        self.signing_key = os.getenv('TOKEN_SIGNING_KEY')
        self.audience = os.getenv('TOKEN_AUDIENCE', None)
        self.issuer = os.getenv('TOKEN_ISSUER', None)
        self.leeway = timedelta(seconds=30)
        self.json_encoder = None
        self.access_token_expiry = timedelta(minutes=15)
        self.refresh_token_expiry = timedelta(days=1)

    
    def get_leeway(self) -> timedelta:
        if self.leeway is None:
            return timedelta(seconds=0)
        elif isinstance(self.leeway, (int, float)):
            return timedelta(seconds=self.leeway)
        elif isinstance(self.leeway, timedelta):
            return self.leeway
        else:
            raise TokenBackendError('Token Leeway is Not Valid.')

    def encode(self, payload: Dict[str, Any], type:str) -> str:
        now = datetime.datetime.now()

        jwt_payload = payload.copy()
        if self.audience is not None:
            jwt_payload['aud'] = self.audience
        if self.issuer is not None:
            jwt_payload['iss'] = self.issuer
        if type == 'access':
            jwt_payload['exp'] = now + self.access_token_expiry
        elif type == 'refresh':
            jwt_payload['exp'] = now + self.refresh_token_expiry
        else:
            jwt_payload['exp'] = now 

        jwt_payload['iat'] = now

        token = jwt.encode(
            jwt_payload,
            self.signing_key,
            algorithm=self.algorithm,
            json_encoder=self.json_encoder
        )

        if isinstance(token, bytes):
            return token.decode('utf-8')
        return token
    
    
    def decode(self, token, verify:bool = True) -> Dict[str, Any]:
        try:
            return jwt.decode(
                token,
                algorithms=[self.algorithm],
                audience=self.audience,
                issuer=self.issuer,
                leeway=self.get_leeway(),
                options={
                    'verify_aud' : self.audience is not None,
                    'verify_signature' : verify,
                },
            )
        except InvalidTokenError as e:
            raise TokenBackendError('Invalid Token Specified')
        

