from rest_framework.parsers import JSONParser

class RequestParser(JSONParser):
    def  parse(self, stream, media_type=None, parser_context=None):
        data = super().parse(stream, media_type, parser_context)
        return self.remove_whitespace(data)
    
    def remove_whitespace(self, data):
        if isinstance(data, list):
            return [self.remove_whitespace(item) for item in data]
        elif isinstance(data, dict):
            return {key:self.remove_whitespace(value) for key,value in data.items()}
        elif isinstance(data, str):
            return data.strip()
        else:
            return data
        