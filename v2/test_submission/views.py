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

	return JsonResponse(res, safe=False)

