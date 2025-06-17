from django.db import models # type: ignore
from django.utils import timezone # type: ignore
from django.conf import settings # type: ignore


class Task(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Task2(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class TelegramMessage(models.Model):
    chat_id = models.BigIntegerField()
    username = models.CharField(max_length=150, null=True, blank=True)
    first_name = models.CharField(max_length=150, null=True, blank=True)
    message_text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name or self.username}: {self.message_text[:20]}"
