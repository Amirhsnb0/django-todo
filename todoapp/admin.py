from django.contrib import admin
from django.contrib.admin.helpers import Fieldset
from django.contrib.admin.options import ModelAdmin
from .models import todoItem

class AuthorAdmin(admin.ModelAdmin):
    pass
admin.site.register(todoItem, AuthorAdmin)