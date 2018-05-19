from django.db import models


# Create your models here.
class Classcast_test_submission(models.Model):
    student_id = models.IntegerField(null=False, primary_key=True)
    xblock_id = models.CharField(max_length=255, primary_key=True)
    num_attempts = models.IntegerField()
    num_skips = models.IntegerField()
    num_incorrect_attempts = models.IntegerField()
    average_time_attempt = models.FloatField()
    average_time_skip = models.FloatField()
    timestamp = models.DateTimeField()
    correctly_attempted_in_test = models.BooleanField()
    correctly_attempted_in_gym = models.BooleanField()

    class Meta:
        db_table = 'classcast_test_submissions'

    def __str__(self):
        return u'%s %s' % (str(self.student_id), str(self.xblock_id))