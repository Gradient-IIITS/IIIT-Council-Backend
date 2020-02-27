from django.urls import path
from ..view.education import *

urlpatterns = [
    path('btech', education_btech, name='education_b_tech'),
    path('mtech', education_m_tech, name='education_m_tech'),
    path('ms', education_m_s, name='education_m_s'),
    path('phd', education_ph_d, name='education_p_hd'),
]
