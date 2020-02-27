from django.urls import path
from ..view.collaboration import *

urlpatterns = [
  path('mou', collab_mou_view, name='collab_mou'),
  path('student_exchange', collab_student_exchange_view, name='collab_student_exchange'),
]
