from django.http import HttpResponse
import models
import api
from django.http import JsonResponse

def hello(request):
   text = """<h1>welcome to my app !</h1>"""
   return HttpResponse(text)


def allsubmissions(request, user_id):
   
	res = models.Classcast_test_submission.objects.filter(student_id=user_id)
	# res = api.get_all_student_test_submission(user_id)

	return JsonResponse(res)


def newsubmission(request, user_id):

	s1 = models.Classcast_test_submission(student_id=user_id, xblock_id='abcd', num_attempts=1, 
		num_skips=0, num_incorrect_attempts=0, average_time_attempt=None, average_time_skip=None, timestamp=None)

	s1.save()

	return JsonResponse({status: True})
