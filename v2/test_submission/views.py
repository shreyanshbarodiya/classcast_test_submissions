from django.http import HttpResponse
import models
import api
from django.http import JsonResponse
from django.core import serializers

def hello(request):
   text = """<h1>welcome to my app !</h1>"""
   return HttpResponse(text)


def allsubmissions(request, user_id):
   
	res = models.Classcast_test_submission.objects.all()
	res_json = serializers.serialize('json', res)
	return HttpResponse(res_json, content_type='application/json')

def newsubmission(request, user_id):

	s1 = models.Classcast_test_submission(student_id=user_id, xblock_id='abcd', num_attempts=1, 
		num_skips=0, num_incorrect_attempts=0, average_time_attempt=None, average_time_skip=None, timestamp=None)

	s1.save()

	return JsonResponse({'status': 'True'})

def curruser(request):

	if request.user.is_authenticated():
		res = request.user.id
	else:
		res = 'Not authenticated'
	return HttpResponse(res)