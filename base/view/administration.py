from django.shortcuts import render, redirect


def admistr_directors_view(request):
    return render(request, 'administration/directors.html', context={'active': 'admistr_directors'})

def adminstr_deans_view(request):
    return render(request, 'administration/deans.html', context={'active': 'admistr_deans'})

def admistr_registrars_view(request):
    return render(request, 'administration/registrars.html', context={'active': 'admistr_registrars'})
