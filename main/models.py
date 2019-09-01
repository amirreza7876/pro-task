from django.db import models
from django.contrib.auth.models import User
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


class GroupTask(models.Model):
    active = models.BooleanField(default=True)
    private_key = models.CharField(max_length=128, default='0000')
    public_key = models.CharField(max_length=128, default='1111')
    member = models.ManyToManyField(User, related_name='groups_in')
    admin = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=255)
    subject = models.CharField(max_length=355)
    private = models.BooleanField(default=False)

    def __str__(self):
        return '{} by {}'.format(self.name, self.admin)

    def get_absolute_url(self):
        return reverse('main:group', args=[self.id])
