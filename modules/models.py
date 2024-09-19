from django.db import models


class Module(models.Model):
    module_id = models.AutoField(primary_key=True)
    trainer_id = models.IntegerField()
    module_name = models.CharField(max_length=20)
    total_marks = models.IntegerField()
    date_created = models.DateField(auto_now_add=True)
    due_date = models.DateField()

    def __str__(self):
        return f'{self.module_name} {self.total_marks}'
