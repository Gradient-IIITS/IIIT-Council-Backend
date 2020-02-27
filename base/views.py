from django.shortcuts import render


# Create your views here.


def home_view(request):
    return render(request, 'base/home.html')


def about_view(request):
    return render(request, 'about/about_iiit.html', context={'active': 'about'})


def about_iiit_act_view(request):
    return render(request, 'about/iiit_act.html', context={'active': 'about_iiit_act'})


def about_ppp_partners_view(request):
    return render(request, 'about/ppp_partners.html', context={'active': 'about_ppp_partners'})


def about_system_review_reports_view(request):
    return render(request, 'about/iiit_syst_review_report.html', context={'active': 'about_system_review_reports'})


def about_administrative_structure_view(request):
    return render(request, 'about/admins_structure.html', context={'active': 'about_administrative_structure'})


def about_history_view(request):
    return render(request, 'about/history.html', context={'active': 'about_history'})
