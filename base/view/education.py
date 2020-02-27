from django.shortcuts import render, redirect


def education_btech(request):
    return render(request, 'education/b_tech.html', context={'active': 'education_b_tech'})


def education_m_tech(request):
    return render(request, 'education/m_tech.html', context={'active': 'education_m_tech'})


def education_m_s(request):
    return render(request, 'education/m_s.html', context={'active': 'education_m_s'})


def education_ph_d(request):
    return render(request, 'education/ph_d.html', context={'active': 'education_ph_d'})
