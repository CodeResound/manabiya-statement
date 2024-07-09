import json

from manabiyacentral.utility.helpers import SanitizeFields
from manabiyacentral.handlers.errorHandler.api_exceptions import SanitizerException

class Sanitize:
    @staticmethod
    def create_statement(request):
        expected_fields = [
            'folder_name1',
            'folder_name2',
            'file_name',
            'template_json',
            'type',
            'doc_count'
        ]

        filtered_data = SanitizeFields.filter(request=request, expected_fields=expected_fields)

        template_json = filtered_data.pop('template_json', None)

        if template_json:
            try:
                template_json_dict = json.loads(template_json)
                if not isinstance(template_json_dict, dict):
                    raise SanitizerException('Template JSON Format Invalid')
            except (json.JSONDecodeError, TypeError) as e:
                raise SanitizerException('Template JSON Format Invalid')
            
            filtered_data['template_json'] = template_json_dict

        
        return filtered_data
    
    @staticmethod
    def create_wodadoc(request):
        expected_fields = [
            'folder_name1',
            'folder_name2',
            'file_name',
            'template_json',
            'type',
            'doc_count'
        ]

        filtered_data = SanitizeFields.filter(request=request, expected_fields=expected_fields)

        template_json = filtered_data.pop('template_json', None)
    
        if template_json:
            try:
                template_json_dict = json.loads(template_json)
                if not isinstance(template_json_dict, dict):
                    raise SanitizerException('Template JSON Format Invalid')
            except (json.JSONDecodeError, TypeError) as e:
                raise SanitizerException('Template JSON Format Invalid')
            
            filtered_data['template_json'] = template_json_dict

        
        return filtered_data
