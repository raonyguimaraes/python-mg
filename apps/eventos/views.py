# Create your views here.

from django.shortcuts import render, get_object_or_404

from .models import Evento

def detalhe(request, id, template='eventos/detalhe.html'):
    evento = get_object_or_404(Evento, pk=id)
    programacao = evento.programacao_set.all()
    organizadores = evento.organizadores.all()
    return render(request, template,
    	{'evento': evento, 'programacao': programacao, 'organizadores': organizadores})

