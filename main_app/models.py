from django.db import models
from django.conf import settings


class Task(models.Model):
   
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    label = models.CharField(max_length=150)
    updated = models.DateTimeField(auto_now=True)
    is_completed = models.BooleanField(default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        related_name="task")

    class Meta:
        app_label = "main_app"
        db_table = "task"
        verbose_name = "task"
        verbose_name_plural = "tasks"

    def __str__(self):
        return self.name