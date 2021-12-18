from django.db import models

class JobPosition(models.Model):
    start_date = models.DateTimeField('date started')
    end_date = models.DateTimeField('date ended')
    company = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
