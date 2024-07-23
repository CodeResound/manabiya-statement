from django.db import models
from manabiyacentral.models import DateTimeModel


class Folder(DateTimeModel):
    code = models.CharField(max_length=255, unique=True, blank=True, editable=False)
    name = models.CharField(max_length=50)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='child', null=True, blank=False)

    class Meta:
        db_table = 'folder'
    
    def __str__(self) -> str:
        return f'{self.code} :: {self.name}'
    
    def save(self, *args, **kwargs):
        if not self.pk:
            if not self.parent:
                self.generate_first_level_code()
            else:
                self.generate_child_code()
        super().save(*args, **kwargs)
    

    def generate_first_level_code(self):
        if self.parent is None:
            last_code = Folder.objects.filter(parent=None).order_by('-code').first()
            if last_code:
                self.code = self.increment_code(last_code.code)
            else:
                self.code = "1"
    
    def generate_child_code(self):
        parent_code = self.parent.code
        last_child_code = self.parent.child.last()
        if last_child_code:
            self.code = parent_code + '-' + self.increment_code(last_child_code.code.split('-')[1])
        else:
            self.code = parent_code + '-1'
    

    def increment_code(self, code_part):
        try:
            new_code_part = str(int(code_part) + 1)
        except ValueError:
            new_code_part = '1'
        return new_code_part



class Statements(DateTimeModel):
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    template = models.JSONField()
    type = models.CharField(max_length=100)
    bank = models.CharField(max_length=100)

    class Meta:
        db_table = 'statements'
        unique_together = ('folder', 'name')


class StatementLogs(DateTimeModel):
    statement = models.ForeignKey(Statements, on_delete=models.CASCADE)
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    template = models.JSONField()
    type = models.CharField(max_length=100)
    bank = models.CharField(max_length=100)

    class Meta:
        db_table = 'statements_logs'


class WodaDocs(DateTimeModel):
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    template = models.JSONField()
    type = models.CharField(max_length=100)
    municipality = models.CharField(max_length=100)

    class Meta:
        db_table = 'woda_docs'
        unique_together = ('folder','name')


class WodaLogs(DateTimeModel):
    wodadoc = models.ForeignKey(WodaDocs, on_delete=models.CASCADE)
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    template = models.JSONField()
    type = models.CharField(max_length=100)
    municipality = models.CharField(max_length=100)

    class Meta:
        db_table = 'wodadocs_logs'


class Signatures(DateTimeModel):
    set = models.CharField(max_length=255)
    template = models.CharField(max_length=255)
    value = models.CharField(max_length=512)
    class Meta:
        db_table = 'signatures'
        unique_together = ('template','value')
        
