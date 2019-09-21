from django.db import models
from django.contrib.auth.models import User, Group
from django.urls import reverse
import random
import string


# User.add_to_class("company_name", models.CharField(max_length=128, null=True, blank=True))


class Request(models.Model):
    text = models.TextField(max_length=256)
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='requests')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='offers')
    team = models.ForeignKey('Team', on_delete=models.CASCADE, related_name='reqtou', default=None, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'req from {} to {}'.format(self.from_user, self.to_user)

    class Meta:
        ordering = ('-date',)

class TeamTask(models.Model):
    STATUS_CHOICES = [
    ('DN', 'Done'),
    ('OD', 'On Doing'),
    ('ST', 'Stuck'),
    ]
    PRIORITY_CHOICES = [
    ('M','Medium'),
    ('H','High'),
    ('L','Low'),
    ('BE','Best effort'),
    ]
    active = models.BooleanField(default=True)
    done = models.BooleanField(default=False)
    team = models.ForeignKey('Team', on_delete=models.CASCADE, related_name='team_tasks', default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks_created')
    text = models.TextField(max_length=512)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='DN')
    priority = models.CharField(max_length=2, choices=PRIORITY_CHOICES, default='M')
    assignee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks_todo', default=None, null=True)
    # like = models.ManyToManyField(User, related_name='likes')

    def __str__(self):
        return 'task by {}'.format(self.user)
    # 
    # def get_absolute_url(self):
    #     return reverse('main:single_task', args=[self.id])

    class Meta:
        ordering = ('-created_date',)


class Team(models.Model):
    def randomString(strlen=20):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(strlen))

    search_id = models.CharField(max_length=40, default=randomString())
    secret_key = models.CharField(max_length=128, default='secret')
    member = models.ManyToManyField(User, related_name='workat')
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='team_creator')
    creator_email = models.EmailField(verbose_name='E-mail',max_length=256, blank=True)
    name = models.CharField(verbose_name='Company Name', max_length=256, unique=True)
    description = models.CharField(max_length=512)
    active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        pass
        # permissions = (
        #     ('add_singletask', 'can add task'),
        #     ('delete_singletask', 'can delete task'),
        #     ('change_singletask', ' can edit task')
        # )

    def __str__(self):
        # owners = ", ".join(str(seg) for seg in self.owner.all())
        return '{} by {}'.format(self.name, self.creator)

    def get_absolute_url(self):
        return reverse('main:team_detail', args=[self.id])



#
# class SingleTask(models.Model):
#     active = models.BooleanField(default=True)
#     done = models.BooleanField(default=False)
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='singletasks')
#     text = models.TextField()
#     created_date = models.DateTimeField(auto_now_add=True)
#     updated_date = models.DateTimeField(auto_now=True)
#     like = models.ManyToManyField(User, related_name='likes')
#
#     def __str__(self):
#         return 'task by {}'.format(self.user)
#
#     def get_absolute_url(self):
#         return reverse('main:single_task', args=[self.id])
#
#     class Meta:
#         ordering = ('-created_date',)
#
#
# class CompanyGroup(models.Model):
#     name = models.CharField(max_length=128, default=None, null=True)
#     team = models.ForeignKey('Team', on_delete=models.CASCADE, related_name='groups', default=None, null=True)
#     member = models.ManyToManyField(User, related_name='groups_in')
#     admin = models.ForeignKey(User, related_name='groups_own', on_delete=models.SET_NULL, null=True)
#     private_key = models.CharField(max_length=128, default='0000')
#     active = models.BooleanField(default=True)
#     admin_key = models.CharField(max_length=128, default='1111')
#
#     def __str__(self):
#         return '{} by {}'.format(self.name, self.admin)
#
#     def get_absolute_url(self):
#         return reverse('main:group_detail', args=[self.id])
