from django.forms import modelform_factory
from django.shortcuts import render

from htmx_django.apps.core.models import Filme


def filme_view(request):
    context = {
        'form': modelform_factory(Filme, fields='__all__'),
        'filmes': Filme.objects.all()
    }
    return render(request, 'exemplo2/filmes.html', context=context)


def create_filme(request):
    if request.POST:
        nome = request.POST.get('nome')
        diretor = request.POST.get('diretor')
        ano = request.POST.get('ano')

        Filme.objects.create(nome=nome, diretor=diretor, ano=ano)

    return render(request, 'exemplo2/filme-list.html', context={'filmes': Filme.objects.all()})


def render_update_filme(request, filme_id):
    filme = Filme.objects.get(id=filme_id)

    form = modelform_factory(Filme, fields='__all__')(instance=filme)

    return render(request, 'exemplo2/filme-update.html', context={'form': form, 'filme': filme})


def update_filme(request, filme_id):
    nome = request.POST.get('nome')
    diretor = request.POST.get('diretor')
    ano = request.POST.get('ano')

    Filme.objects.filter(id=filme_id).update(nome=nome, diretor=diretor, ano=ano)

    return filme_view(request)


def delete_filme(request, filme_id):
    filme = Filme.objects.get(id=filme_id)

    filme.delete()

    return render(request, 'exemplo2/filme-list.html', context={'filmes': Filme.objects.all()})
