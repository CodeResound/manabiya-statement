from rest_framework import serializers

from .models import (
    Statements,  
    WodaDocs,
    Signatures
)

class StatementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statements
        fields = '__all__'


class StatementFolderCountSerializer(serializers.Serializer):
    folder_name1 = serializers.CharField()
    count = serializers.IntegerField()


class StatementFolder2CountSerializer(serializers.Serializer):
    folder_name2 = serializers.CharField()
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
    folder_name1 = serializers.CharField()
    count = serializers.IntegerField()


class WodaFolder2CountSerializer(serializers.Serializer):
    folder_name2 = serializers.CharField()
    count = serializers.IntegerField()


class WodaFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = WodaDocs
        fields = ('id','file_name','type')


class SignaturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Signatures
        fields = '__all__'