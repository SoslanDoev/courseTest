from django.db import models
from testing.models import Testing

class Question(models.Model):
    testing = models.ForeignKey(Testing, on_delete=models.CASCADE, related_name="questions", verbose_name="Тестирование")
    title = models.TextField(max_length=500, verbose_name="Текст вопроса")
    ball = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Балл за правильный ответ")
    """ Timestamps """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  
    
    class Meta:
        verbose_name = "Вопросы"
        verbose_name_plural = "Вопросы"
        ordering = ["created_at"]