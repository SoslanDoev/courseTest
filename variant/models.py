from django.db import models
from question.models import Question

class Variant(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="question", verbose_name="Вопросы")
    title = models.CharField(max_length=100, verbose_name="Текст варианта ответа")
    is_correct = models.BooleanField(default=False, verbose_name="Правильность ответа")
    ball = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Балл за правильный ответ")
    """ Timestamps """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  

    class Meta:
        verbose_name = "Варианты ответов"
        verbose_name_plural = "Варианты ответов"
        ordering = ["created_at"]