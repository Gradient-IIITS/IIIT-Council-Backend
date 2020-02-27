from django.shortcuts import render, redirect


def admiss_info_view(request):
    return render(request, 'admission/information.html', context={'active': 'admiss_info'})

def admiss_links_view(request):
    return render(request, 'admission/links.html', context={'active': 'admiss_links'})

def admiss_entrance_view(request):
    return render(request, 'admission/entrance_exam.html', context={'active': 'admiss_entrance'})
