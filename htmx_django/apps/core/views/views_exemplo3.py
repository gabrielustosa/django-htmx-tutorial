from django.http import HttpResponse
from django.shortcuts import render

from htmx_django.apps.core.models import Filme


def search_filme_view(request):
    return render(request, 'exemplo3/search_filmes_view.html')


def search_filme(request):
    search = request.POST.get('search')

    query = Filme.objects.filter(nome__icontains=search)

    if not query.exists() or search == "":
        return HttpResponse('<h5 class="text-center pt-4">Não foi encontrado nenhum resultado </h5>')

    return render(request, 'exemplo3/result_filmes.html', context={'filmes': query.all()})

