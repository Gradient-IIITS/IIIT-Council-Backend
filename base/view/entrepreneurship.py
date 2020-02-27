from django.shortcuts import render


def e_cell(request):
    return render(request, 'entrepreneurship/e_cell.html', context={'about': 'e_cell'})


def innovation_centre(request):
    return render(request, 'entrepreneurship/innovation_centre.html', context={'about': 'innovation_centre'})
