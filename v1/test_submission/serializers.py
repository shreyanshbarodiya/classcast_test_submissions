""" Django REST Framework Serializers """
from rest_framework import serializers

class StudentTestSubmissionSerializer(serializers.Serializer):
    """ Serializer for Submissions  """
    user_id = serializers.CharField()

