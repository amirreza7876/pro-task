# Generated by Django 2.2.3 on 2019-09-12 18:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0003_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('secret_key', models.CharField(default='secret', max_length=128)),
                ('creator_email', models.EmailField(blank=True, max_length=256, verbose_name='E-mail')),
                ('name', models.CharField(max_length=256, unique=True, verbose_name='Company Name')),
                ('description', models.CharField(max_length=512)),
                ('active', models.BooleanField(default=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='co_creator', to=settings.AUTH_USER_MODEL)),
                ('employee', models.ManyToManyField(related_name='workat', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ManyToManyField(related_name='co_own', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('add_singletask', 'can add task'), ('delete_singletask', 'can delete task'), ('change_singletask', ' can edit task')),
            },
        ),
        migrations.CreateModel(
            name='CompanyGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=128, null=True)),
                ('private_key', models.CharField(default='0000', max_length=128)),
                ('active', models.BooleanField(default=True)),
                ('admin_key', models.CharField(default='1111', max_length=128)),
                ('admin', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='groups_own', to=settings.AUTH_USER_MODEL)),
                ('company', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='groups', to='main.Company')),
                ('member', models.ManyToManyField(related_name='groups_in', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GroupTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('done', models.BooleanField(default=False)),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='main.CompanyGroup')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created_date',),
            },
        ),
        migrations.AddField(
            model_name='singletask',
            name='done',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='singletask',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='singletasks', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
    ]