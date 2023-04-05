from django.contrib import admin
from todoitem.models import Task

# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display=['t_id','task']