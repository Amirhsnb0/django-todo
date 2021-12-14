from django import forms
from django.db import models
from django.db.models import fields 
from .models import todoItem

class todoforms (forms.ModelForm):
    class Meta :
        model= todoItem
        fields = ['work','date']