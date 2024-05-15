from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=150, verbose_name="Название")
    """ Timestamps """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Автор"
        ordering = ["created_at"]