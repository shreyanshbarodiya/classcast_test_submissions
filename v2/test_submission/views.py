from django.http import HttpResponse
# from models import Classcast_test_submission
import api
from django.http import JsonResponse

def hello(request):
   text = """<h1>welcome to my app !</h1>"""
   return HttpResponse(text)


def allsubmissions(request, user_id):
   
	#Read all entries

	# objects = Classcast_test_submission.objects.all()
	# res ='Printing all submissions in the DB : <br>'

	# for elt in objects:
	# 	res += elt.xblock_id+"<br>"   

	res = api.get_all_student_test_submission(user_id)

	#return JsonResponse({'foo':'bar'})
	return JsonResponse(res, safe=False)

