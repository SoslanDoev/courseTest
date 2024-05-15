from django.db import models

class Discipline(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    """ Timestamps """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  
    
    class Meta:
        verbose_name = "Предметы"
        verbose_name_plural = "Предметы"
        ordering = ["created_at"]
    