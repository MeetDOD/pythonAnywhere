# Generated by Django 4.1.5 on 2023-01-25 13:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0030_alter_notification_notif_for'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detail', models.TextField()),
                ('add_time', models.DateTimeField(auto_now_add=True)),
                ('teacher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.teacher')),
            ],
            options={
                'verbose_name_plural': '11. Quizs',
            },
        ),
        migrations.CreateModel(
            name='QuizQuestions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questions', models.CharField(max_length=200)),
                ('ans1', models.CharField(max_length=200)),
                ('ans2', models.CharField(max_length=200)),
                ('ans3', models.CharField(max_length=200)),
                ('ans4', models.CharField(max_length=200)),
                ('right_ans', models.CharField(max_length=200)),
                ('add_time', models.DateTimeField(auto_now_add=True)),
                ('quiz', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.quiz')),
            ],
            options={
                'verbose_name_plural': '12. Quiz Question&answer ',
            },
        ),
        migrations.CreateModel(
            name='CourseQuiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(auto_now_add=True)),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.course')),
                ('quiz', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.quiz')),
            ],
            options={
                'verbose_name_plural': '13. Course Quiz ',
            },
        ),
    ]
