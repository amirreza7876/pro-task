# Generated by Django 2.2.5 on 2019-09-25 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20190925_1538'),
    ]

    operations = [
        migrations.AddField(
            model_name='teamtask',
            name='title',
            field=models.CharField(default='', max_length=128),
        ),
        migrations.AlterField(
            model_name='team',
            name='search_id',
            field=models.CharField(default='xlldvrrdwqzhtaaygrrd', max_length=40),
        ),
    ]
