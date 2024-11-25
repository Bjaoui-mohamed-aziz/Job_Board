from django.db import models

# Create your models here.


JOB_TYPE = (
        ('Full Time', 'Full Time'),
        ('Part Time', 'Part Time'),
        ('Freelance', 'Freelance'),
    )
class Job(models.Model):  # table
    title = models.CharField(max_length=100)  # column
    job_type = models.CharField(max_length=15, choices=JOB_TYPE)  # column
    description = models.TextField(max_length=1000)  # column
    published_at = models.DateTimeField(auto_now=True)  # column
    Vacancy = models.IntegerField(default=1)  # column
    salary = models.IntegerField(default=0)  # column
    experience = models.IntegerField(default=1)  # column

    def __str__(self):
        return self.title
