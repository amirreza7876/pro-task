# Generated by Django 2.2.3 on 2019-09-03 11:52

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0017_auto_20190903_1050'),
    ]

    operations = [
        migrations.AddField(
            model_name='companygroup',
            name='name',
            field=models.CharField(default=None, max_length=128, null=True),
        ),
        migrations.RemoveField(
            model_name='company',
            name='owner',
        ),
        migrations.AddField(
            model_name='company',
            name='owner',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
