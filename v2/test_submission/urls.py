"""
test submission v1 URL specification
"""
from django.conf.urls import url, patterns
import views

urlpatterns = patterns(
    '',
    # url(r'^allsubmissions/(?P<user_id>[A-Za-z0-9_.-]+)/$', views.AllTestSubmissions.as_view()),
    url(r'^hello$', views.hello, name = 'hello'),
    url(r'^curruser$', views.curruser, name = 'curruser'),
	url(r'^allsubmissions/(?P<user_id>[A-Za-z0-9_.-]+)/$', views.allsubmissions, name='allsubmissions'),
	url(r'^newsubmission/(?P<user_id>[A-Za-z0-9_.-]+)/$', views.newsubmission, name='newsubmission'),
)
