from django.db import models

class Group(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    """ Timestamps """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  
    
    class Meta:
        verbose_name = "Группы"
        verbose_name_plural = "Группы"
        ordering = ["created_at"]