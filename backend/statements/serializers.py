from rest_framework import serializers

from .models import (
    Statements,  
    WodaDocs,
)

class StatementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statements
        fields = '__all__'


class StatementFolderCountSerializer(serializers.Serializer):
    folder_name = serializers.CharField()
    count = serializers.IntegerField()


class StatementFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statements
        fields = ('id','file_name','type')


class WodaDocSerializer(serializers.ModelSerializer):
    class Meta:
        model = WodaDocs
        fields  = '__all__'

        
class WodaFolderCountSerializer(serializers.Serializer):
    folder_name = serializers.CharField()
    count = serializers.IntegerField()


class WodaFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = WodaDocs
        fields = ('id','file_name','type')


