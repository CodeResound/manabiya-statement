from django.db import models
from manabiyacentral.models import DateTimeModel

class Statements(DateTimeModel):

    student_name = models.CharField(max_length=100)
    file_name = models.CharField(max_length=100)
    template_name = models.CharField(max_length=100)
    template1_json = models.JSONField()
    template2_json = models.JSONField()
    status = models.CharField(max_length=10)
    folder = models.CharField(max_length=100, unique=True)
    
    class Meta:
        db_table = 'statements'