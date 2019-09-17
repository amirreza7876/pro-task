# Generated by Django 2.2.5 on 2019-09-14 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20190914_1419'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grouptask',
            name='group',
        ),
        migrations.AddField(
            model_name='grouptask',
            name='team',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='main.Team'),
        ),
        migrations.DeleteModel(
            name='CompanyGroup',
        ),
    ]
