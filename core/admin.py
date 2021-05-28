from django.contrib import admin
from .models import (User,
                     Task,
                     Event,
                     TaskCategory,
                     EventCategory,
                     EventState,
                     TaskState)
# Register your models here.

@admin.register(User, Task, Event, TaskCategory, TaskState, EventState, EventCategory)
class UserAdmin(admin.ModelAdmin):
    pass