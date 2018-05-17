"""
test submission API URI specification.
"""
from django.conf.urls import include, url, patterns

urlpatterns = patterns(
    '',
    url(r'^', include('classcast_test_submissions.v1.test_submission.urls')),
)
