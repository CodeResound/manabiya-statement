import os

from datetime import timedelta

import jwt
from jwt import InvalidTokenError

from typing import Dict, Any
from .utils import (
   aware_utcnow,
   datetime_to_epoch
)
from manabiyacentral.handlers.errorHandler.api_exceptions import TokenBackendError, AccessTokenExpiredError


class TokenBackend:
    def __init__(self) -> None:
        self.algorithm = os.getenv('TOKEN_ALGORITHM')
        self.signing_key = os.getenv('TOKEN_SIGNING_KEY')
        self.audience = os.getenv('TOKEN_AUDIENCE', None)
        self.issuer = os.getenv('TOKEN_ISSUER', None)
        self.leeway = timedelta(seconds=30)
        self.json_encoder = None
        self.access_token_expiry = timedelta(minutes=1)
        self.refresh_token_expiry = timedelta(days=2)

    
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
        now = aware_utcnow()

        jwt_payload = payload.copy()
        if self.audience is not None:
            jwt_payload['aud'] = self.audience
        if self.issuer is not None:
            jwt_payload['iss'] = self.issuer
        if type == 'access':
            jwt_payload['exp'] = datetime_to_epoch(now + self.access_token_expiry)
        elif type == 'refresh':
            jwt_payload['exp'] = datetime_to_epoch(now + self.refresh_token_expiry)
        else:
            jwt_payload['exp'] = datetime_to_epoch(now) 

        jwt_payload['iat'] = datetime_to_epoch(now)

        
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
                self.signing_key,
                algorithms=[self.algorithm],
                audience=self.audience,
                issuer=self.issuer,
                leeway=self.get_leeway(),
                options={
                    'verify_aud' : self.audience is not None,
                    'verify_signature' : verify,
                },
            )

        except jwt.ExpiredSignatureError:
            raise AccessTokenExpiredError()

        except InvalidTokenError as e:
            raise TokenBackendError('Invalid Token Specified')
        

