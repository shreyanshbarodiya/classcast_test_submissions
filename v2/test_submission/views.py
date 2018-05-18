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

def newsubmission(request):
	if not request.user.is_authenticated():
		return JsonResponse({'status': 'False', 'Message': 'Not authenticated'})

	if(request.method == "GET"):
		return JsonResponse({'status': 'False', 'Message': 'Get request'})
	else:
		student_id = request.user.id
		xblock_id = request.POST['xblock_id']
		attempted = request.POST['attempted']
		correctly_attempted = request.POST['correctly_attempted']
		time_taken = request.POST['time_taken']
		timestamp = request.POST['timestamp']

		if models.Classcast_test_submission.objects.filter(student_id=student_id, xblock_id=xblock_id).exists():
			entry = models.Classcast_test_submission.objects.get(student_id=student_id, xblock_id=xblock_id)
			if(attempted==1):
				entry.num_attempts += 1
				entry.num_incorrect_attempts += 1 - correctly_attempted
				entry.average_time_attempt = ((entry.average_time_attempt*(entry.num_attempts-1)) + time_taken)/entry.num_attempts
				entry.timestamp = timestamp
			else:
				entry.num_skips += 1
				entry.average_time_skip = ((entry.average_time_skip*(entry.num_skips-1)) + time_taken)/entry.num_skips
				entry.timestamp = timestamp
			entry.save()
		else:
			if(attempted==1):
				s1 = models.Classcast_test_submission(student_id=student_id, 
					xblock_id=xblock_id, num_attempts=1, num_skips=0, 
					num_incorrect_attempts=1-correctly_attempted , average_time_attempt=time_taken, average_time_skip=0, timestamp=timestamp)
			else:
				s1 = models.Classcast_test_submission(student_id=student_id, 
					xblock_id=xblock_id, num_attempts=0, num_skips=1, 
					num_incorrect_attempts=0 , average_time_attempt=0, average_time_skip=time_taken, timestamp=timestamp)
			s1.save()

	return JsonResponse({'status': 'True'})

def curruser(request):

	if request.user.is_authenticated():
		res = request.user.id
	else:
		res = 'Not authenticated'
	return HttpResponse(res)