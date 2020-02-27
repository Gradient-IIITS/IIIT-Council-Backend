from django.urls import path
from ..view.admission import *

urlpatterns = [
  path('info', admiss_info_view, name='admiss_info'),
  path('links', admiss_links_view, name='admiss_links'),
  path('entrance', admiss_entrance_view, name='admiss_entrance'),
]
