import logging
from django.db import IntegrityError
from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework import status

logger = logging.getLogger('errors')

def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first
    response = exception_handler(exc, context)
    
    # Log the exception with context information
    logger.error(f"Exception occurred: {exc} | Context: {context}")

    if isinstance(exc, IntegrityError):
        return Response({
            'type' : 'Integrity Error',
            'message' : 'Other records are linked to this record. Delete them first.'
        }, status=status.HTTP_400_BAD_REQUEST)

    # If the response exists, modify it
    if response is not None:
        # Always include a 'type' parameter in the response
        if isinstance(exc, ValidationError):
            response.data['type'] = 'Validation Error'
        else:
            response.data['type'] = 'Error'
        
        # Map 'detail' to 'message' for standardization
        if 'detail' in response.data:
            response.data['message'] = response.data.pop('detail')
        
        # Handle custom message for non_field_errors if they exist
        if isinstance(exc, ValidationError) and 'non_field_errors' in exc.detail:
            response.data['non_field_errors'] = ["Data Already Exists!"]
    
    # If no response exists, create a generic error response
    if response is None:
        response = Response({
            'type': 'Internal Server Error',
            'message': 'Something went wrong. Please contact support.'
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return response