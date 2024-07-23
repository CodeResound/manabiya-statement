from rest_framework import serializers

from .models import (
    Statements,  
    WodaDocs,
    Signatures,
    StatementLogs,
    WodaLogs,
    Folder
)

class FolderSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField(read_only=True)  
    class Meta:
        model = Folder
        fields = ['id','name','code','parent','children']

    def get_children(self, obj):
        children = Folder.objects.filter(parent=obj)
        return FolderSerializer(children, many=True).data
    


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


class StatementLogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatementLogs
        fields = '__all__'

class WodaLogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = WodaLogs
        fields = '__all__'
        