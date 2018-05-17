from rest_framework import generics
from api import *
from serializers import StudentTestSubmissionSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.http import Http404
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from oauth2_provider.ext.rest_framework.authentication import OAuth2Authentication
from rest_framework.throttling import UserRateThrottle

# Create your views here.

class UserThrottle(UserRateThrottle):

    rate = '40/minute'

    def allow_request(self, request, view):
        return super(UserThrottle, self).allow_request(request, view)



class AllTestSubmissions(generics.RetrieveAPIView):
    """
        **Use Case**

            Get all the students for a specific course.

        **Example Requests**

              GET /api/courses/v2/detail/{user_id}

        **Response Values**

            On success with Response Code <200>

            * course_name: Name of the course

            * course_organization: The organization specified for the course.

            * course_run: The run of the course

            * students:

                * id: The unique identifier for the student.

                * username: Username of the student

                * email: Email of the student

                * grade: Overall grade of the student in the course

                * total_score: Total score of the student in the course

                * is_active: Shows whether the student is active or not
                    1: if student is active
                    0: if student is not active

                * last_login: The date and time at which the student was last active

         **ERROR RESPONSES**

                * Response Code <404> ORGANIZATION NOT FOUND
                * Response Code <403> FORBIDDEN

        """
    serializer_class = StudentTestSubmissionSerializer
    permission_classes = (IsAdminUser,)
    authentication_classes = (SessionAuthentication, BasicAuthentication, OAuth2Authentication)
    throttle_classes = (UserThrottle,)

    def get_object(self):
        try:
            list = get_all_student_test_submission(self.kwargs['user_id'])
            list['user_id']
            return list
        except:
            raise Http404            
