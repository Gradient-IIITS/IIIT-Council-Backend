from django.urls import path, include
from base.views import home_view, about_view, about_iiit_act_view, about_ppp_partners_view, \
  about_system_review_reports_view, about_administrative_structure_view, about_history_view

urlpatterns = [
  path('', home_view, name='home_page'),
  path('about', about_view, name='about'),
  path('about/iiit_act', about_iiit_act_view, name='about_iiit_act'),
  path('about/history', about_history_view, name='about_history'),
  path('about/administrative_structure', about_administrative_structure_view,
       name='about_administrative_structure'),
  path('about/system_review_reports', about_system_review_reports_view,
       name='about_system_review_reports'),
  path('about/ppp_partners', about_ppp_partners_view, name='about_ppp_partners'),
  path('education/', include('base.url.education')),
  path('entrepreneurship/', include('base.url.entrepreneurship')),
  path('research/', include('base.url.research')),
  path('forum/', include('base.url.forum')),
  path('administration/', include('base.url.administration')),
  path('admission/', include('base.url.admission')),
  path('collaboration/', include('base.url.collaboration')),
]
