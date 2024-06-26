from rest_framework import status
from rest_framework.exceptions import APIException

class BaseCustomException(APIException):
    def __init__(self, detail, code):
        super().__init__(detail, code)
        self.detail = detail
        self.code = code


class SerializerException(BaseCustomException):
    def __init__(self, detail=None, code=None):
        detail = detail or "Serializer Error"
        code = code or status.HTTP_400_BAD_REQUEST
        super().__init__(detail, code)

class SanitizerException(BaseCustomException):
    def __init__(self, detail=None, code=None):
        detail = detail or "Invalid Data Format"
        code = code or status.HTTP_405_METHOD_NOT_ALLOWED
        super().__init__(detail, code)
    

class ConfigFileNotFound(BaseCustomException):
    def __init__(self, detail=None, code=None):
        detail = detail or "Configuration File Not Found"
        code = code or status.HTTP_404_NOT_FOUND
        super().__init__(detail, code)

class UnSupportedFormat(BaseCustomException):
    def __init__(self, detail=None, code=None):
        detail = detail or "Format of Data is Not Supported"
        code = code or status.HTTP_415_UNSUPPORTED_MEDIA_TYPE
        super().__init__(detail, code)


class FunctionalException(BaseCustomException):
    def __init__(self, detail=None, code=None):
        detail = detail or "Something Went Wrong. Please Contact Microworld for Support."
        code = code or status.HTTP_500_INTERNAL_SERVER_ERROR
        super().__init__(detail, code) 


class MethodNotAllowed(BaseCustomException):
    def __init__(self, detail=None, code=None):
        detail = detail or "Something Went Wrong."
        code = code or status.HTTP_405_METHOD_NOT_ALLOWED
        super().__init__(detail, code)


class LoginException(BaseCustomException):
    def __init__(self, detail=None, code=None):
        detail = detail or "Invalid Credentials. Please Try Again."
        code = code or status.HTTP_405_METHOD_NOT_ALLOWED
        super().__init__(detail, code)


class EmailException(BaseCustomException):
    def __init__(self, detail=None, code=None):
        detail = detail or "Unable to Send Email."
        code = code or status.HTTP_502_BAD_GATEWAY
        super().__init__(detail, code)


class NotVerifiedOTPException(BaseCustomException):
    def __init__(self, detail=None, code=None):
        detail = detail or "Account Not Verified Yet."
        code = code or status.HTTP_401_UNAUTHORIZED
        super().__init__(detail, code)


class InvalidApiException(BaseCustomException):
    def __init__(self, detail=None, code=None):
        detail = detail or "Invalid API Request."
        code = code or status.HTTP_400_BAD_REQUEST
        super().__init__(detail, code)       


class BannedUserException(BaseCustomException):
    def __init__(self, detail=None, code=None):
        detail = detail or "This Account Has Been Suspended. Please Contact Microworld For Support."
        code = code or status.HTTP_403_FORBIDDEN
        super().__init__(detail, code)


class NotVerifiedUser(BaseCustomException):
    def __init__(self, detail=None, code=None):
        detail = detail or "User Has Not Been Verified. Please Verify Account."
        code = code or status.HTTP_401_UNAUTHORIZED
        super().__init__(detail, code)


class InvalidToken(BaseCustomException):
    def __init__(self, detail=None, code=None):
        detail = detail or "Invalid Token"
        code = code or status.HTTP_401_UNAUTHORIZED
        super().__init__(detail, code)


class UnAuthorizedUser(BaseCustomException):
    def __init__(self, detail=None, code=None):
        detail = detail or "UnAuthorized User"
        code = code or status.HTTP_401_UNAUTHORIZED
        super().__init__(detail, code)


class AlreadyExists(BaseCustomException):
    def __init__(self, detail=None, code=None):
        detail = detail or "Record Already Exists"
        code = code or status.HTTP_405_METHOD_NOT_ALLOWED
        super().__init__(detail, code)


class NotFound(BaseCustomException):
    def __init__(self, detail=None, code=None):
        detail = detail or "Record Not Found"
        code = code or status.HTTP_404_NOT_FOUND
        super().__init__(detail, code)