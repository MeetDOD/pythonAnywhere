# Generated by Django 4.1.5 on 2023-01-25 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0031_quiz_quizquestions_coursequiz'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='title',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
