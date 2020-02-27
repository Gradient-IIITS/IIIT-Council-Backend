from django.shortcuts import render


def research_projects(request):
    return render(request, 'research/projects.html', context={'active': 'research_projects'})


def research_patents(request):
    return render(request, 'research/patents.html', context={'active': 'research_patents'})


def research_publications(request):
    return render(request, 'research/publications.html', context={'active': 'research_publications'})


def research_facilities(request):
    return render(request, 'research/facilities.html', context={'active': 'research_facilities'})
