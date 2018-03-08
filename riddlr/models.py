from django.db import models
from django.contrib.auth.models import User

class Riddle(models.Model):
    riddle_id = models.IntegerField(unique=True)
    question = models.CharField(150)
    details = models.CharField(800)
    answer = models.CharField(30)
    date_posted = models.DateField()
    difficulty = models.IntegerField()
    rating = models.IntegerField()
    num_answers = models.IntegerField()

    author = models.ForeignKey(User, on_delete=models.CASCADE)



    class Meta:
        verbose_name_plural = 'riddles'
    
    def __str__(self):
        return self.question

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    date_joined = models.DateField()
    score = models.IntegerField()
    karma = models.IntegerField()
    guess_ratio = models.FloatField()
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username
