from django.shortcuts import render
from django.http import HttpResponse

def home_view(request):
    """
    View para a página inicial do ArqConcursos.
    """
    return HttpResponse("<h1>Bem-vindo ao ArqConcursos!</h1><p>Sua plataforma para concursos de Arquitetura.</p>")

# Você pode renderizar um template HTML mais tarde:
# def home_view(request):
#     return render(request, 'core/home.html', {})