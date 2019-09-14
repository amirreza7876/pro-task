from django.db import models
from django.contrib.auth.models import User, Group
from django.urls import reverse


User.add_to_class("company_name", models.CharField(max_length=128, null=True, blank=True))


class SingleTask(models.Model):
    active = models.BooleanField(default=True)
    done = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='singletasks')
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    like = models.ManyToManyField(User, related_name='likes')

    def __str__(self):
        return 'task by {}'.format(self.user)

    def get_absolute_url(self):
        return reverse('main:single_task', args=[self.id])

    class Meta:
        ordering = ('-created_date',)





class CompanyGroup(models.Model):
    name = models.CharField(max_length=128, default=None, null=True)
    company = models.ForeignKey('Company', on_delete=models.CASCADE, related_name='groups', default=None, null=True)
    member = models.ManyToManyField(User, related_name='groups_in')
    admin = models.ForeignKey(User, related_name='groups_own', on_delete=models.SET_NULL, null=True)
    private_key = models.CharField(max_length=128, default='0000')
    active = models.BooleanField(default=True)
    admin_key = models.CharField(max_length=128, default='1111')

    def __str__(self):
        return '{} by {}'.format(self.name, self.admin)

    def get_absolute_url(self):
        return reverse('main:group_detail', args=[self.id])

class GroupTask(models.Model):
        active = models.BooleanField(default=True)
        done = models.BooleanField(default=False)
        group = models.ForeignKey(CompanyGroup, on_delete=models.CASCADE, related_name='tasks')
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
    secret_key = models.CharField(max_length=128, default='secret')
    employee = models.ManyToManyField(User, related_name='workat')
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='co_creator')
    owner = models.ManyToManyField(User, related_name='co_own')
    creator_email = models.EmailField(verbose_name='E-mail',max_length=256, blank=True)
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
        # owners = ", ".join(str(seg) for seg in self.owner.all())
        return '{} by {}'.format(self.name, self.creator)

    def get_absolute_url(self):
        return reverse('main:company_detail', args=[self.id])
