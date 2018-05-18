from django.db import models


# Create your models here.
class Classcast_test_submission(models.Model):
    student_id = models.IntegerField(null=False)
    xblock_id = models.CharField(max_length=255)
    num_attempts = models.IntegerField()
    num_skips = models.IntegerField()
    num_incorrect_attempts = models.IntegerField()
    average_time_attempt = models.DurationField()
    average_time_skip = models.DurationField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'classcast_test_submissions'
