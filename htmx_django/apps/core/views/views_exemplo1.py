import uuid

from random import choice

from django.shortcuts import render


def example_click_load(request):
    return render(request, 'exemplo1/click_to_load.html')


def replace_example(request):
    nomes = ['gabriel', 'arthur', 'nicolas', 'fátima', 'maria', 'ana']
    random_nome = choice(nomes)

    context = {
        'pessoa': [random_nome, f'{random_nome}@test.org', uuid.uuid1()]
    }

    return render(request, 'exemplo1/replace_example.html', context=context)
