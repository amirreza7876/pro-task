# Generated by Django 2.2.5 on 2019-09-19 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='search_id',
            field=models.CharField(default='fgtvvrxsimjuvsgliybd', max_length=40),
        ),
    ]
