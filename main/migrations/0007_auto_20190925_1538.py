# Generated by Django 2.2.5 on 2019-09-25 15:38

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20190919_0829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='search_id',
            field=models.CharField(default='hyemfvsblkqgnvtqdtsc', max_length=40),
        ),
        migrations.AlterField(
            model_name='teamtask',
            name='assignee',
            field=models.EmailField(default=None, max_length=254, null=True, verbose_name=django.contrib.auth.models.User),
        ),
    ]
