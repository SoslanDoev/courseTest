from django.db import models
from testing.models import Testing
from group.models import Group

class Schedule_test(models.Model):
    testing = models.ForeignKey(Testing, on_delete=models.CASCADE, related_name="testing", verbose_name="Тестирование")
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="group", verbose_name="Группа")
    time_start = models.DateTimeField(verbose_name="Время начала тестирования")
    time_end = models.DateTimeField(verbose_name="Время конца тестирования")
    """ Timestamps """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  

    class Meta:
        verbose_name = "Настройки работы теста"
        verbose_name_plural = "Настройки работы теста"
        ordering = ["created_at"]