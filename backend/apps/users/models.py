from django.db import models
from django.contrib.auth.models import AbstractUser # Use AbstractUser para estender o modelo de usuário padrão
from apps.core.models import AbstractBaseModel

class CustomUser(AbstractUser):
    # Adicione campos personalizados aqui se precisar, por exemplo:
    # area_interesse = models.CharField(max_length=100, blank=True)
    # nivel_experiencia = models.CharField(max_length=50, blank=True)
    pass # Por enquanto, usamos apenas os campos padrão de AbstractUser

class ProgressoUsuario(AbstractBaseModel):
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='progresso')
    sub_topico = models.ForeignKey('content.SubTopico', on_delete=models.CASCADE) # Referência ao SubTopico
    concluido = models.BooleanField(default=False)

    class Meta:
        unique_together = ('usuario', 'sub_topico') # Garante que um usuário só tenha 1 progresso por subtópico
        verbose_name = "Progresso do Usuário"
        verbose_name_plural = "Progressos dos Usuários"

    def __str__(self):
        return f"Progresso de {self.usuario.username} em {self.sub_topico.nome}"