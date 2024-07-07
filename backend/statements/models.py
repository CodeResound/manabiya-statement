from django.db import models
from manabiyacentral.models import DateTimeModel

class Statements(DateTimeModel):
    folder_name = models.CharField(max_length=100)
    file_name = models.CharField(max_length=100)
    template_json = models.JSONField()
    type = models.CharField(max_length=100)
    doc_count = models.SmallIntegerField()

    class Meta:
        db_table = 'statements'
        unique_together = ('folder_name','file_name')


class StatementLogs(DateTimeModel):
    statement = models.ForeignKey(Statements, on_delete=models.CASCADE)
    folder_name = models.CharField(max_length=100)
    file_name = models.CharField(max_length=100)
    template_json = models.JSONField()
    doc_count = models.SmallIntegerField()

    class Meta:
        db_table = 'statements_logs'


class WodaDocs(DateTimeModel):
    folder_name = models.CharField(max_length=100)
    file_name = models.CharField(max_length=100)
    template_json = models.JSONField()
    type = models.CharField(max_length=100)
    doc_count = models.CharField(max_length=100)
    class Meta:
        db_table = 'woda_docs'
        unique_together = ('folder_name','file_name')


class WodaLogs(DateTimeModel):
    wodadoc = models.ForeignKey(WodaDocs, on_delete=models.CASCADE)
    folder_name = models.CharField(max_length=100)
    file_name = models.CharField(max_length=100)
    template_json = models.JSONField()

    class Meta:
        db_table = 'wodadocs_logs'
