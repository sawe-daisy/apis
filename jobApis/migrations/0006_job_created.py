# Generated by Django 3.2.6 on 2021-08-12 01:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('jobApis', '0005_rename_edeucation_level_job_education_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
