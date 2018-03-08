from django.db import models
from django.contrib.auth.models import User


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
    riddle_id = models.IntegerField(unique=True)
    question = models.CharField(max_length=150)
    details = models.CharField(max_length=800)
    answer = models.CharField(max_length=30)
    date_posted = models.DateField()
    difficulty = models.IntegerField()
    rating = models.IntegerField()
    num_answers = models.IntegerField()

    author = models.ForeignKey(User, models.CASCADE)

    answered_by = models.ManyToManyField(UserProfile, through='UserAnswer')

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
