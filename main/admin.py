from django.contrib import admin
from .models import *


# @admin.register(SingleTask)
# class SingleTaskAdmin(admin.ModelAdmin):
#     pass
#

# @admin.register(CompanyGroup)
# class CompanyGroupAdmin(admin.ModelAdmin):
#     pass


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    pass


@admin.register(TeamTask)
class TeamTaskAdmin(admin.ModelAdmin):
    pass

@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    pass
