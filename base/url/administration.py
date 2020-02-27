from django.urls import path
from ..view.administration import *

urlpatterns = [
  path('directors', admistr_directors_view, name='admistr_directors'),
  path('deans', adminstr_deans_view, name='admistr_deans'),
  path('registrars', admistr_registrars_view, name='admistr_registrars'),
]
