# Generated by Django 2.2.5 on 2019-09-14 18:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20190914_1834'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='employee',
            new_name='member',
        ),
    ]