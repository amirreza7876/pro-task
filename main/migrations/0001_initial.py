# Generated by Django 2.2.5 on 2019-09-18 15:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('secret_key', models.CharField(default='secret', max_length=128)),
                ('creator_email', models.EmailField(blank=True, max_length=256, verbose_name='E-mail')),
                ('name', models.CharField(max_length=256, unique=True, verbose_name='Company Name')),
                ('description', models.CharField(max_length=512)),
                ('active', models.BooleanField(default=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='team_creator', to=settings.AUTH_USER_MODEL)),
                ('member', models.ManyToManyField(related_name='workat', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TeamTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('done', models.BooleanField(default=False)),
                ('text', models.TextField(max_length=512)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('DN', 'Done'), ('OD', 'On Doing'), ('ST', 'Stuck')], default='DN', max_length=2)),
                ('priority', models.CharField(choices=[('M', 'Medium'), ('H', 'High'), ('L', 'Low'), ('BE', 'Best effort')], default='M', max_length=2)),
                ('assignee', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tasks_todo', to=settings.AUTH_USER_MODEL)),
                ('team', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='team_tasks', to='main.Team')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks_created', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created_date',),
            },
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=256)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requests', to=settings.AUTH_USER_MODEL)),
                ('team', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reqtou', to='main.Team')),
                ('to_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='offers', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-date',),
            },
        ),
    ]
