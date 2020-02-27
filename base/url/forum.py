from django.urls import path
from django.conf.urls import url
from ..view.forum import *

urlpatterns = [
  path('chairman', forum_chairman_view, name='forum_chairman'),
  path('secretary', forum_secretary_view, name='forum_secretary'),
  path('members', forum_members_view, name='forum_members'),
  path('meeting_minutes', forum_meeting_minutes_view, name='forum_meeting_minutes'),
]
