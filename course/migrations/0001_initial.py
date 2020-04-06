# Generated by Django 3.0.4 on 2020-04-06 15:20

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(max_length=255)),
                ('status', models.CharField(choices=[('i', 'in progress'), ('f', 'finish'), ('n', 'not yet')], default='n', max_length=1)),
                ('room_name', models.CharField(default='#', max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='CourseSubject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=255)),
                ('duration', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Supervisor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='TraineeCourseSubject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(default=datetime.date.today)),
                ('is_active', models.BooleanField(default=False)),
                ('status', models.CharField(choices=[('i', 'in progress'), ('f', 'finish'), ('n', 'not yet')], default='n', max_length=1)),
                ('course_subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.CourseSubject')),
            ],
        ),
    ]
