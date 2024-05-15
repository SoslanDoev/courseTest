from django.db import models
from author.models import Author
from discipline.models import Discipline

class Testing(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE, related_name="discipline", verbose_name="Дисциплина")
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="author", verbose_name="Автор")
    """ Timestamps """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  

    class Meta:
        verbose_name = "Тестирование"
        verbose_name_plural = "Тестирование"
        ordering = ["created_at"]