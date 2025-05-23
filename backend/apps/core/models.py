from django.db import models

class AbstractBaseModel(models.Model):
    """
    Modelo abstrato que fornece campos comuns como created_at e updated_at.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-created_at'] # Ordena por data de criação decrescente