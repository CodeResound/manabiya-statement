import json

from manabiyacentral.utility.helpers import SanitizeFields
from manabiyacentral.handlers.errorHandler.api_exceptions import SanitizerException

class Sanitize:
    @staticmethod
    def create_statement(request):
        expected_fields = [
            'folder',
            'name',
            'template',
            'type',
            'bank'
        ]

        filtered_data = SanitizeFields.filter(request=request, expected_fields=expected_fields)

        template_json = filtered_data.pop('template', None)

        if template_json:
            try:
                template_json_dict = json.loads(template_json)
                if not isinstance(template_json_dict, dict):
                    raise SanitizerException('Template JSON Format Invalid')
            except (json.JSONDecodeError, TypeError) as e:
                raise SanitizerException('Template JSON Format Invalid')
            
            filtered_data['template'] = template_json_dict

        
        return filtered_data
    
    @staticmethod
    def create_wodadoc(request):
        expected_fields = [
            'folder',
            'name',
            'template',
            'type',
            'municipality'
        ]

        filtered_data = SanitizeFields.filter(request=request, expected_fields=expected_fields)

        template_json = filtered_data.pop('template', None)
    
        if template_json:
            try:
                template_json_dict = json.loads(template_json)
                if not isinstance(template_json_dict, dict):
                    raise SanitizerException('Template JSON Format Invalid')
            except (json.JSONDecodeError, TypeError) as e:
                raise SanitizerException('Template JSON Format Invalid')
            
            filtered_data['template'] = template_json_dict

        
        return filtered_data
