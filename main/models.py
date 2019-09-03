from django.db import models
from django.contrib.auth.models import User, Group
from django.urls import reverse


class SingleTask(models.Model):
    active = models.BooleanField(default=True)
    done = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    # like = models.ManyToManyField(User, related_name='likes')

    def __str__(self):
        return 'task by {}'.format(self.user)

    def get_absolute_url(self):
        return reverse('main:single_task', args=[self.id])

    class Meta:
        ordering = ('-created_date',)


class Company(models.Model):
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    owner_email = models.EmailField(verbose_name='E-mail',max_length=256, blank=True)
    name = models.CharField(verbose_name='Company Name', max_length=256, unique=True)
    description = models.CharField(max_length=512)
    active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        permissions = (
            ('add_singletask', 'can add task'),
            ('delete_singletask', 'can delete task'),
            ('change_singletask', ' can edit task')
        )

    def __str__(self):
        return '{} by {}'.format(self.name, self.owner.username)

    def get_absolute_url(self):
        return reverse('main:company_detail', id=self.id)


class CompanyGroup(models.Model):
    member = models.ManyToManyField(User, related_name='group')
    admin = models.ForeignKey(Company, related_name='company_groups', on_delete=models.SET_NULL, null=True)
    private_key = models.CharField(max_length=128, default='0000')
    active = models.BooleanField(default=True)
    admin_key = models.CharField(max_length=128, default='1111')
