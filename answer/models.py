from django.db import models
from student.models import Student
from variant.models import Variant

class Answer(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="student", verbose_name="Студент")
    variant = models.ForeignKey(Variant, on_delete=models.CASCADE, related_name="variant", verbose_name="Вариант")
    answer = models.CharField(max_length=100, verbose_name="Открытый ответ")
    host = models.CharField(max_length=100, verbose_name="Хост, с которого был передан ответ")
    """ Timestamps """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  

    class Meta:
        verbose_name = "Ответы"
        verbose_name_plural = "Ответы"
        ordering = ["created_at"]