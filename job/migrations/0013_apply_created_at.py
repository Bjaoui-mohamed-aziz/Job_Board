# Generated by Django 5.1.3 on 2024-12-10 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0012_apply_job'),
    ]

    operations = [
        migrations.AddField(
            model_name='apply',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]