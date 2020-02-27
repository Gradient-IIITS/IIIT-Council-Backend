from django.urls import path
from ..view.research import *


urlpatterns = [
    path('projects', research_projects, name='research_projects'),
    path('patents', research_patents, name='research_patents'),
    path('publications', research_publications, name='research_publications'),
    path('facilities', research_facilities, name='research_facilities'),
]
