# Generated by Django 4.1.5 on 2023-01-24 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_studentassignment'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentassignment',
            name='student_status',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
