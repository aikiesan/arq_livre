from django.db import models
from apps.core.models import AbstractBaseModel # Importe seu modelo base

class Disciplina(AbstractBaseModel):
    nome = models.CharField(max_length=200, unique=True)
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome

class Topico(AbstractBaseModel):
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, related_name='topicos')
    nome = models.CharField(max_length=255)
    ordem = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['ordem']
        unique_together = ('disciplina', 'nome')

    def __str__(self):
        return f"{self.disciplina.nome} - {self.nome}"

class SubTopico(AbstractBaseModel):
    topico = models.ForeignKey(Topico, on_delete=models.CASCADE, related_name='sub_topicos')
    nome = models.CharField(max_length=255)
    conteudo_markdown = models.TextField() # Aqui você armazenará o texto formatado em Markdown
    ordem = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['ordem']
        unique_together = ('topico', 'nome')

    def __str__(self):
        return f"{self.topico.nome} - {self.nome}"

class Questao(AbstractBaseModel):
    sub_topico = models.ForeignKey(SubTopico, on_delete=models.CASCADE, related_name='questoes')
    pergunta = models.TextField()
    alternativa_a = models.TextField()
    alternativa_b = models.TextField()
    alternativa_c = models.TextField()
    alternativa_d = models.TextField()
    RESPOSTA_CHOICES = [
        ('a', 'A'), ('b', 'B'), ('c', 'C'), ('d', 'D')
    ]
    resposta_correta = models.CharField(max_length=1, choices=RESPOSTA_CHOICES)
    justificativa = models.TextField() # Aquele seu conteúdo comentado

    def __str__(self):
        return self.pergunta[:70] + "..."