# Generated by Django 4.1.5 on 2023-01-22 07:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_alter_studentcourseenrollment_course_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveBigIntegerField(default=0)),
                ('reviews', models.TextField(null=True)),
                ('review_time', models.DateTimeField(auto_now_add=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.student')),
            ],
        ),
    ]
