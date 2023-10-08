from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin

from .models import MenuModel


@admin.register(MenuModel)
class CountryAdmin(DjangoMpttAdmin):
    prepopulated_fields = {'named_url': ('name',)}
