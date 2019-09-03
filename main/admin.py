from django.contrib import admin
from .models import *


@admin.register(SingleTask)
class SingleTaskAdmin(admin.ModelAdmin):
    pass


@admin.register(CompanyGroup)
class CompanyGroupAdmin(admin.ModelAdmin):
    pass


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    pass
