import argon2, os, string, random, jwt, datetime

from uuid import uuid4
from argon2.exceptions import Argon2Error, VerifyMismatchError
from manabiyacentral.handlers.errorHandler.api_exceptions import (
    FunctionalException,
    UnSupportedFormat,
    SanitizerException
)

class Argon2:
    def __init__(self, time_cost=2, memory_cost=1024, parallelism=1, hash_len=32):
        self.hasher = argon2.PasswordHasher(
            time_cost = time_cost,
            memory_cost=memory_cost,
            parallelism=parallelism,
            hash_len=hash_len
        )
    
    def hash_password(self, password):
        try:
            return self.hasher.hash(password)
        except Argon2Error as e:
            raise FunctionalException(f'Hashing Error - {str(e)}')
    
    def verify_password(self, stored_hash, password):
        try:
            return self.hasher.verify(stored_hash, password)
        except VerifyMismatchError:
            return False
        except Argon2Error as e:
            raise FunctionalException(f'Verify Error - {str(e)}')


class ImageSanitizer():
    def __init__(self) -> None:
        self.max_size = 3 * 1024 * 1024
        self.formats = ('.jpg','.jpeg','.png','.webp','.gfif','.gif','.pdf')
        self.max_length = 20
    
    def validate_image(self, file):
        if file.size > self.max_size:
            raise UnSupportedFormat('File Too Large. Please Upload a File Less than 3 MB')
        ext = os.path.splitext(file.name)[1]
        if not ext.lower() in self.formats:
            raise UnSupportedFormat('File Format Not Supported. Please Upload a Valid Format.')
        return file

    def generate_unique_name(self, file_name):
        ext = file_name.split('.')[-1]
        new_name = f'{uuid4().hex}.{ext}'
        if len(new_name) > self.max_length:
            new_name = f'{new_name[:self.max_length-len(ext)-1]}.{ext}'
        return new_name


class Generators:
    @staticmethod
    def generate_uid(max_length):
        unique_id = str(uuid4().hex)
        while len(unique_id) < max_length:
            unique_id = random.choice(string.ascii_letters+string.digits)
        return unique_id[:max_length]
    
    @staticmethod
    def generate_otp(max_length):
        characters = string.ascii_uppercase + string.digits
        otp = ''.join(random.choices(characters, k=max_length)) 
        return otp


class SanitizeFields:
    @staticmethod
    def filter(request, expected_fields):
        filtered_data = {key: value for key, value in request.data.items() if key in expected_fields}
        return filtered_data
    
    @staticmethod
    def integrity(request, compulsory_fields):
        for field in compulsory_fields:
            if field in request.data:
                raise SanitizerException('Mandatory Fields are Missing. Please Contact Support.')
