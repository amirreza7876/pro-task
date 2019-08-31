from django.contrib import admin
from .models import *


@admin.register(SingleTask)
class SingleTaskAdmin(admin.ModelAdmin):
    pass

@admin.register(GroupTask)
class GroupTaskAdmin(admin.ModelAdmin):
    pass
