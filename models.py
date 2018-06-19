from django.db import models
import datetime

# Create your models here.
class Classcast_test_submission(models.Model):
    student_id = models.IntegerField(null=False, primary_key=True)
    xblock_id = models.CharField(max_length=255, primary_key=True)
    num_attempts = models.IntegerField()
    num_skips = models.IntegerField()
    num_incorrect_attempts = models.IntegerField()
    average_time_attempt = models.FloatField()
    average_time_skip = models.FloatField()
    curr_status = models.IntegerField()
    timestamp = models.DateTimeField()
    correctly_attempted_in_test = models.BooleanField()
    correctly_attempted_in_gym = models.BooleanField()

    class Meta:
        db_table = 'classcast_test_submissions'

    def __str__(self):
        return u'%s %s' % (str(self.student_id), str(self.xblock_id))


class Classcast_questions(models.Model):
    xblock_id = models.CharField(max_length=255, primary_key=True)
    question_type = models.CharField()
    standard = models.IntegerField()
    stream = models.CharField()
    subject = models.CharField()
    goal = models.CharField()
    difficulty = models.IntegerField()
    marks = models.IntegerField()
    chapter = models.CharField()
    topic = models.CharField()
    subtopic = models.CharField()
    question_image = models.CharField()
    option1_image = models.CharField()
    option2_image = models.CharField()
    option3_image = models.CharField()
    option4_image = models.CharField()
    num_correct_submissions = models.IntegerField()
    average_time_to_answer = models.FloatField()
    tags = models.CharField()
    exam_appearances = models.IntegerField()
    num_deliveries = models.IntegerField()
    num_skipped = models.IntegerField()

    class Meta:
        db_table = 'classcast_questions'

    def __str__(self):
        return u'%s %s %s' % (str(self.subject), str(self.topic), str(self.xblock_id))

class Classcast_student_info(models.Model):
    student_id = models.IntegerField(null=False, primary_key=True)
    pincode = models.IntegerField()
    standard = models.IntegerField()
    stream = models.CharField()
    marks_scored_in_last_degree = models.FloatField()
    total_time_spent_on_platform = models.FloatField()
    active_status = models.CharField()
    last_active = models.DateTimeField()
    total_karma_points = models.FloatField()
    phone_number = models.CharField()
    
    class Meta:
        db_table = 'classcast_student_info'


class Classcast_karma_history(models.Model):
    student_id = models.IntegerField(null=False, primary_key=True)
    date = models.DateField(primary_key=True, default=datetime.date.today)
    karma_points = models.FloatField() 

    class Meta:
        db_table = 'classcast_karma_history'