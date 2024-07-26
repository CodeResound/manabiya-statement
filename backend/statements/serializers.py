from rest_framework import serializers

from .models import (
    Statements,  
    WodaDocs,
    Signatures,
    StatementLogs,
    WodaLogs,
    Folder
)

class StatementListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statements
        fields = [
            'id',
            'name',
            'bank',
            'type'
        ]


class WodaDocListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WodaDocs
        fields = [
            'id',
            'name',
            'type',
            'municipality'
        ]

class FolderListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Folder
        fields = [
            'id',
            'name',
            'code',
            'parent',
        ]


class FolderSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField(read_only=True)  
    statements = serializers.SerializerMethodField(read_only=True)
    wodadoc = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Folder
        fields = ['id','name','code','parent','children','statements','wodadoc']

    def get_children(self, obj):
        children = Folder.objects.filter(parent=obj)
        return FolderListSerializer(children, many=True).data
    
    def validate_parent(self, value):
        if value is None:
            raise serializers.ValidationError('Parent Field Cannot be Null.')
        return value
    
    def get_statements(self, obj):
        statements = Statements.objects.filter(folder=obj)
        return StatementListSerializer(statements, many=True).data
    
    def get_wodadoc(self, obj):
        wodadoc = WodaDocs.objects.filter(folder=obj)
        return WodaDocListSerializer(wodadoc, many=True).data


class StatementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statements
        fields = '__all__'


class StatementFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statements
        fields = ('id','name','type')


class WodaDocSerializer(serializers.ModelSerializer):
    class Meta:
        model = WodaDocs
        fields  = '__all__'

    

class WodaFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = WodaDocs
        fields = ('id','name','type')


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
        