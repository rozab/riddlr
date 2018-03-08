from django.db import models
from django.contrib.auth.models import User
import json


class UserProfile(models.Model):
    user = models.OneToOneField(User, models.CASCADE)

    date_joined = models.DateField()
    score = models.IntegerField()
    karma = models.IntegerField()
    guess_ratio = models.FloatField()
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username


class Riddle(models.Model):
    # note there is an auto generated id field
    question = models.CharField(max_length=150)
    details = models.CharField(max_length=800)
    date_posted = models.DateField(auto_now_add=True)
    difficulty = models.IntegerField(default=75)
    rating = models.IntegerField(default=0)
    num_answers = models.IntegerField(default=0)

    # TODO remove null=True at some point
    author = models.ForeignKey(User, models.CASCADE, null=True)
    answered_by = models.ManyToManyField(UserProfile, through='UserAnswer')

    # Set of answers implemented with json
    answers = models.CharField(max_length=300, default="")

    def set_answers(self, answer_list):
        self.answers = json.dumps(answer_list)

    def get_answers(self):
        return json.loads(self.answers)

    class Meta:
        verbose_name_plural = 'riddles'

    def __str__(self):
        return self.question


class UserAnswer(models.Model):
    user = models.ForeignKey(UserProfile, models.CASCADE)
    riddle = models.ForeignKey(Riddle, models.CASCADE)

    num_tries = models.IntegerField()
    correct = models.BooleanField()
    previous_answer = models.CharField(max_length=30)
