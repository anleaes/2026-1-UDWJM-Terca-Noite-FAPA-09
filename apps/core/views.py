from django.shortcuts import render, get_object_or_404
from catalogo.models import Catalogo


def home(request):
    catalogos = Catalogo.objects.select_related(
        'veiculo', 'veiculo__grupo'
    ).filter(ativo=True).order_by('-destaque', 'preco_diaria')
    
    return render(request, 'core/home.html', {
        'catalogos': catalogos,
    })


def veiculo_detalhe(request, pk):
    catalogo = get_object_or_404(
        Catalogo.objects.select_related('veiculo', 'veiculo__grupo'),
        pk=pk
    )
    return render(request, 'core/veiculo_detalhe.html', {
        'catalogo': catalogo,
    })