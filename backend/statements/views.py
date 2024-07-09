from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser
from rest_framework.decorators import api_view

from django.db.models import Count

from manabiyacentral.middlewares.parsers import RequestParser

from .models import (
    Statements,
    WodaDocs,
    StatementLogs,
    WodaLogs
)

from .sanitizers import Sanitize

from .serializers import (
    StatementsSerializer,
    WodaDocSerializer,
    WodaFolderCountSerializer,
    WodaFolder2CountSerializer,
    StatementFolderCountSerializer,
    StatementFolder2CountSerializer,
    StatementFileSerializer,
    WodaFileSerializer
    )


class StatementView(viewsets.ModelViewSet):
    queryset = Statements.objects.all()
    serializer_class = StatementsSerializer
    parser_classes = [MultiPartParser, RequestParser]

    def create(self, request, *args, **kwargs):
        sanitized_data = Sanitize.create_statement(request=request)
        serializer = self.get_serializer(data=sanitized_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get_distinct_folder(self, request, *args, **kwargs):
        folder_counts = (
            Statements.objects.values('folder_name1').annotate(count=Count('id')).order_by('folder_name1')
        )
        serializer = StatementFolderCountSerializer(folder_counts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def get_distinct_folder2(self, request, *args, **kwargs):
        folder_name1 = request.query_params.get('folder_name1','')
        folder_counts = (
            Statements.objects.filter(folder_name1=folder_name1).values('folder_name2').annotate(count=Count('id')).order_by('folder_name2')
        )
        serializer = StatementFolder2CountSerializer(folder_counts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def get_file_names_for_folder(self, request):
        folder_name = request.query_params.get('folder_name','')
        file_names = Statements.objects.filter(folder_name2=folder_name)
        serializer = StatementFileSerializer(file_names, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def get_recent_statements(self, request):
        recent_statements = (
            Statements.objects.all().order_by('-id')[:10]
        )
        serializer = StatementFileSerializer(recent_statements, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


        
class WodaDocView(viewsets.ModelViewSet):
    queryset = WodaDocs.objects.all()
    serializer_class = WodaDocSerializer
    parser_classes = [MultiPartParser, RequestParser]

    def create(self, request, *args, **kwargs):
        sanitized_data = Sanitize.create_wodadoc(request=request)
        serializer = self.get_serializer(data=sanitized_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get_distinct_folder(self, request, *args, **kwargs):
        folder_counts = (
            WodaDocs.objects.values('folder_name1').annotate(count=Count('id')).order_by('folder_name1')
        )
        serializer = WodaFolderCountSerializer(folder_counts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def get_distinct_folder2(self, request, *args, **kwargs):
        folder_name1 = request.query_params.get('folder_name1','')
        folder_counts = (
            WodaDocs.objects.filter(folder_name1=folder_name1).values('folder_name2').annotate(count=Count('id')).order_by('folder_name2')
        )
        serializer = WodaFolder2CountSerializer(folder_counts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

    def get_file_names_for_folder(self, request):
        folder_name = request.query_params.get('folder_name','') 
        file_names = WodaDocs.objects.filter(folder_name2=folder_name)
        serializer = WodaFileSerializer(file_names, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def get_recent_wodadoc(self, request):
        recent_wodadoc = (
            WodaDocs.objects.all().order_by('-id')[:10]
        )
        serializer = WodaFileSerializer(recent_wodadoc, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def print_and_log_statement(request):
    try:
        statement_id = request.data.get('statement_id')
        statement = Statements.objects.get(id=statement_id)

        StatementLogs.objects.create(
            statement=statement,
            folder_name1=statement.folder_name1,
            folder_name2=statement.folder_name2,
            file_name=statement.file_name,
            template_json=statement.template_json,
            doc_count=statement.doc_count
        )
        
        return Response({'message': 'Statement logged successfully'}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'Something Went Wrong'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def print_and_log_woda(request):
    try:
        wodadoc_id = request.data.get('wodadoc_id')
        wodadoc = WodaDocs.objects.get(id=wodadoc_id)

        WodaLogs.objects.create(
            wodadoc=wodadoc,
            folder_name1=wodadoc.folder_name1,
            folder_name2=wodadoc.folder_name2,
            file_name=wodadoc.file_name,
            template_json=wodadoc.template_json,
            doc_count=wodadoc.doc_count
        )
        
        return Response({'message': 'Woda Document logged successfully'}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'Something Went Wrong'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)  