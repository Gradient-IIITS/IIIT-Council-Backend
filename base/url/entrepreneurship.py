from django.urls import path
from ..view.entrepreneurship import *


urlpatterns = [
    path('e-cell', e_cell, name='e_cell'),
    path('innovation-centre', innovation_centre, name='innovation_centre'),
]
