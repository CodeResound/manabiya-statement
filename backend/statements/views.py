from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser
from rest_framework.decorators import api_view
from rest_framework.decorators import action

from manabiyacentral.middlewares.parsers import RequestParser

from .models import (
    Statements,
    WodaDocs,
    StatementLogs,
    WodaLogs,
    Signatures,
    Folder
)

from .sanitizers import Sanitize

from .serializers import (
    StatementsSerializer,
    WodaDocSerializer,
    StatementFileSerializer,
    WodaFileSerializer,
    SignaturesSerializer,
    StatementLogsSerializer,
    WodaLogsSerializer,
    FolderSerializer
    )

from manabiyacentral.middlewares.auth_token import JWTAuthentication
from manabiyacentral.handlers.errorHandler.api_exceptions import NotFound

class FolderView(viewsets.ModelViewSet):
    queryset = Folder.objects.all()
    serializer_class = FolderSerializer
    parser_classes = [RequestParser,MultiPartParser]

    def list(self, request, *args, **kwargs):
        queryset = Folder.objects.filter(parent=None)
        serializer = self.get_serializer(queryset, many= True)
        return Response(serializer.data)


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
        try:
            statement = Statements.objects.get(id=statement_id)
        except Statements.DoesNotExist:
            raise NotFound()
        
        StatementLogs.objects.create(
            statement=statement,
            folder = statement.folder,
            name=statement.name,
            template=statement.template,
            type = statement.type,
            bank = statement.bank
        )
        
        return Response({'message': 'Statement logged successfully'}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'Something Went Wrong'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def print_and_log_woda(request):
    try:
        wodadoc_id = request.data.get('wodadoc_id')
        try:
            wodadoc = WodaDocs.objects.get(id=wodadoc_id)
        except WodaDocs.DoesNotExist:
            raise NotFound()
        
        WodaLogs.objects.create(
            wodadoc=wodadoc,
            folder = wodadoc.folder,
            name=wodadoc.name,
            template=wodadoc.template,
            type = wodadoc.type,
            municipality = wodadoc.municipality
        )
        
        return Response({'message': 'Woda Document logged successfully'}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'Something Went Wrong'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)  


class SignatureView(viewsets.ModelViewSet):
    queryset = Signatures.objects.all()
    serializer_class = SignaturesSerializer
    parser_classes = [MultiPartParser, RequestParser]


class  StatementLogsView(viewsets.ModelViewSet):
    queryset = StatementLogs.objects.all()
    serializer_class = StatementLogsSerializer
    parser_classes = [RequestParser, MultiPartParser]

    @action(detail=False, methods=['get'])
    def find_by_statement_id(self, request):
        statement_id = request.query_params.get('statement_id')
        if not statement_id:
            return Response({}, status=status.HTTP_204_NO_CONTENT)
        
        logs = StatementLogs.objects.filter(statement_id=statement_id)
        serializer = self.get_serializer(logs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class WodaLogsView(viewsets.ModelViewSet):
    queryset = WodaLogs.objects.all()
    serializer_class = WodaLogsSerializer
    parser_classes = [RequestParser, MultiPartParser]

    @action(detail=False, methods=['get'])
    def find_by_woda_id(self, request):
        wodadoc_id = request.query_params.get('wodadoc_id')
        if not wodadoc_id:
            return Response({}, status=status.HTTP_204_NO_CONTENT)
        
        logs = WodaLogs.objects.filter(wodadoc_id=wodadoc_id)
        serializer = self.get_serializer(logs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

