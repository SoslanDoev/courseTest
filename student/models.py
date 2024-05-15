from django.db import models
from group.models import Group

class Student(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    surname = models.CharField(max_length=100, verbose_name="Фамилия")
    patronymic = models.CharField(max_length=100, verbose_name="Отчество")
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="student", verbose_name="Группа")
    block = models.BooleanField(default=False, verbose_name="Заблокированный")
    login = models.CharField(max_length=100, unique=True, verbose_name="Логин")
    password = models.CharField(max_length=100, verbose_name="Пароль")
    token = models.CharField(max_length=255, default="", unique=True, verbose_name="Токен")
    """ Timestamps """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  

    class Meta:
        verbose_name = "Студенты"
        verbose_name_plural = "Студенты"
        ordering = ["created_at"]
    