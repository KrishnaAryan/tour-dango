from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Photo)
class EmployeeAdmin(admin.ModelAdmin):
    list_display=('id','photo','date',)