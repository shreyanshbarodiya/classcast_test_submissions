from django.http import HttpResponse
import models
from django.http import JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt  
import datetime
from classcast.classcast_search_fetch.models import student_topic_interaction, topics

def hello(request):
   text = """<h1>welcome to my app !</h1>"""
   return HttpResponse(text)


def allsubmissions(request, user_id):
   
	res = models.Classcast_test_submission.objects.all()
	res_json = serializers.serialize('json', res)
	return HttpResponse(res_json, content_type='application/json')

def update_submission_status(entry):
	tmp = 5.0*(entry.num_attempts - entry.num_incorrect_attempts)/((entry.num_attempts + entry.num_skips)*1.0)
	return round(tmp)


#update in classcast_test_submissions table 
#update in classcast_student_info table: karma points - done - only when correctly attempted
#update in classcast_karma_history - done - only when correctly attempted
#update in question's difficulty - ? 
#update in student's chapterwise/subjectwise ranks/marks - ?
@csrf_exempt
def newsubmission(request):
	# if not request.user.is_authenticated():
	# 	return JsonResponse({'status': 'False', 'Message': 'Not authenticated'})

	if(request.method == "GET"):
		return JsonResponse({'status': 'False', 'message': 'Get request'})

	try:

		# student_id = request.user.id
		student_id = int(request.POST.get('student_id'))
		xblock_id = request.POST.get('xblock_id')
		attempted = int(request.POST.get('attempted'))
		correctly_attempted = int(request.POST.get('correctly_attempted'))
		time_taken = float(request.POST.get('time_taken'))
		timestamp = request.POST.get('timestamp')
		appeared_in_test = int(request.POST.get('appeared_in_test'))
		appeared_in_gym = int(request.POST.get('appeared_in_gym'))

		q_info = models.Classcast_questions.objects.get(xblock_id=xblock_id)
		student_info = models.Classcast_student_info.objects.get(student_id=student_id)
		topic_info = topics.objects.get(chapter__standard=q_info.standard, chapter__subject=q_info.subject, chapter__chapter=q_info.chapter, topic_name=q_info.topic)
		
		if student_topic_interaction.objects.filter(student__id=student_id, topic__topic_id=topic_info.topic_id, difficulty=q_info.difficulty).exists():
			s_t_interaction = student_topic_interaction.objects.get(student__id=student_id, topic__topic_id=topic_info.topic_id, difficulty=q_info.difficulty)
		else:
			s_t_interaction = student_topic_interaction(student__id=student_id, topic__topic_id=topic_info.topic_id, difficulty=q_info.difficulty)


		if models.Classcast_karma_history.objects.filter(student_id=student_id, date=datetime.date.today).exists():
			karma_history = models.Classcast_karma_history.objects.get(student_id=student_id, date=datetime.date.today)
		else:
			karma_history = models.Classcast_karma_history(student_id=student_id, date=str(datetime.datetime.strftime(datetime.datetime.today(),'%Y-%m-%d')), karma_points=0)

		# An entry exists in classcast_test_submissions
		if models.Classcast_test_submission.objects.filter(student_id=student_id, xblock_id=xblock_id).exists():
			entry = models.Classcast_test_submission.objects.get(student_id=student_id, xblock_id=xblock_id)
			if(attempted==1):
				entry.num_attempts += 1
				entry.num_incorrect_attempts += 1 - correctly_attempted
				entry.average_time_attempt = ((entry.average_time_attempt*(entry.num_attempts-1)) + time_taken)/entry.num_attempts
				entry.correctly_attempted_in_test = entry.correctly_attempted_in_test or (appeared_in_test and correctly_attempted)
				entry.correctly_attempted_in_gym = entry.correctly_attempted_in_gym or (appeared_in_gym and correctly_attempted)
				s_t_interaction.num_attempts += 1
				s_t_interaction.num_corrects += correctly_attempted
			else:
				entry.num_skips += 1
				entry.average_time_skip = ((entry.average_time_skip*(entry.num_skips-1)) + time_taken)/entry.num_skips
				s_t_interaction.num_skipped += 1
			
			entry.timestamp = timestamp
			entry.curr_status = update_submission_status(entry)
			entry.save()
			s_t_interaction.save()
			return JsonResponse({'status': 'True', 'message': 'Success'})
		
		# A new entry is made in classcast_test_submissions
		else:
			if(attempted==1):
				sub = models.Classcast_test_submission(student_id=student_id, 
					xblock_id=xblock_id, num_attempts=1, num_skips=0, 
					num_incorrect_attempts=1-correctly_attempted , average_time_attempt=time_taken, 
					average_time_skip=0, timestamp=timestamp)
				sub.correctly_attempted_in_test = (appeared_in_test and correctly_attempted)
				sub.correctly_attempted_in_gym = (appeared_in_gym and correctly_attempted)
				sub.curr_status = update_submission_status(sub)
				sub.save()

				s_t_interaction.num_attempts += 1

				# if(correctly_attempted)
				student_info.total_karma_points += q_info.marks*correctly_attempted
				karma_history.karma_points += q_info.marks*correctly_attempted
				s_t_interaction.num_corrects += correctly_attempted

				student_info.save()
				karma_history.save()
				s_t_interaction.save()

			else:
				sub = models.Classcast_test_submission(student_id=student_id, 
					xblock_id=xblock_id, num_attempts=0, num_skips=1, 
					num_incorrect_attempts=0 , average_time_attempt=0, 
					average_time_skip=time_taken, timestamp=timestamp,
					correctly_attempted_in_test=False, correctly_attempted_in_gym=False)			
				sub.curr_status = update_submission_status(sub)
				sub.save()
				s_t_interaction.num_skipped += 1
				s_t_interaction.save()

			return JsonResponse({'status': 'True', 'message': 'Success'})

	except Exception, e:
		return JsonResponse({'status': 'False', 'message': 'Database error'})

def curruser(request):

	if request.user.is_authenticated():
		res = request.user.id
	else:
		res = 'Not authenticated'
	return HttpResponse(res)
