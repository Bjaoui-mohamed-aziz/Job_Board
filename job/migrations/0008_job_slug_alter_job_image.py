# Generated by Django 5.1.3 on 2024-12-06 14:05

import job.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0007_job_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='image',
            field=models.ImageField(upload_to=job.models.image_upload),
        ),
    ]
