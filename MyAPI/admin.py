from django.contrib import admin
from .models import Task, Task2, TelegramMessage
from rest_framework.authtoken.models import Token  # ✅ Correct import

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'completed')
    list_filter = ('completed',)
    search_fields = ('title',)


@admin.register(Task2)
class TaskAdmin2(admin.ModelAdmin):
    list_display = ('title', 'completed', 'created_at')
    list_filter = ('completed',)
    search_fields = ('title',)
    ordering = ('-created_at',)


@admin.register(TelegramMessage)
class TelegramMessageAdmin(admin.ModelAdmin):
    list_display = ('chat_id', 'username', 'first_name', 'message_text', 'timestamp')


@admin.register(Token)  # ✅ Correct usage with DRF's Token
class TokenAdmin(admin.ModelAdmin):
    list_display = ('key', 'user', 'created')
