# Generated by Django 3.1.3 on 2022-03-20 18:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=2000)),
                ('image', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('link', models.CharField(max_length=2000)),
                ('published_on', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Connection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('your_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(max_length=500)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True)),
                ('is_present', models.BooleanField(blank=True, null=True)),
                ('responsibilities_1', models.CharField(blank=True, default=None, max_length=2000)),
                ('responsibilities_2', models.CharField(blank=True, default=None, max_length=2000)),
                ('responsibilities_3', models.CharField(blank=True, default=None, max_length=2000)),
                ('responsibilities_4', models.CharField(blank=True, default=None, max_length=2000)),
                ('company', models.CharField(blank=True, default=None, max_length=200)),
                ('location', models.CharField(blank=True, default=None, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('designation', models.CharField(max_length=500)),
                ('summary', models.CharField(max_length=5000)),
                ('image', models.CharField(max_length=5000)),
                ('email', models.EmailField(max_length=254)),
                ('github_link', models.URLField()),
                ('linkedin_link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('description', models.CharField(max_length=2000)),
                ('github_link', models.CharField(max_length=2000)),
                ('keywords', models.CharField(default='', max_length=1000)),
                ('image', models.CharField(max_length=1000)),
                ('tech_stack_1', models.CharField(default='', max_length=1000)),
                ('tech_stack_2', models.CharField(default='', max_length=1000)),
                ('tech_stack_3', models.CharField(default='', max_length=1000)),
                ('tech_stack_4', models.CharField(default='', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.CharField(max_length=1000)),
            ],
        ),
    ]
