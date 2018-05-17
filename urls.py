"""
classcast test submissions URI specification.
Patterns here should simply point to version-specific patterns.
"""
from django.conf.urls import include, url, patterns

urlpatterns = patterns(
    '',

    url(r'^v1/', include('classcast_test_submissions.v1.urls')),
    url(r'^v2/', include('classcast_test_submissions.v2.urls')),
)
