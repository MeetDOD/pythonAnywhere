# Generated by Django 4.1.5 on 2023-01-22 08:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_courserating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courserating',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.course'),
        ),
        migrations.AlterField(
            model_name='courserating',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.student'),
        ),
    ]
