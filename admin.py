# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Classcast_test_submission,Classcast_karma_history,Classcast_student_info

# Register your models here.
admin.site.register(Classcast_karma_history)
admin.site.register(Classcast_test_submission)
admin.site.register(Classcast_student_info)
