from django.db import models
from django.contrib.auth.models import User
import json
from PIL import Image


class UserProfile(models.Model):
    user = models.OneToOneField(User, models.CASCADE)

    date_joined = models.DateField(auto_now_add=True)
    score = models.IntegerField(default=0)
    karma = models.IntegerField(default=0)
    # null for no answers and -1 for inf
    guess_ratio = models.FloatField(null=True)
    picture = models.ImageField(upload_to='profile_images', null=True, blank=True)
    riddles = models.TextField(blank=True)  # temporary field type, need to solve which type / how riddles are gonna be handled

    def crop_picture(self):
        if self.picture:
            path = self.picture.path
            im = Image.open(path)
            width, height = im.size
            new_size = min(width,height)

            if width == height:
                return
            elif width > height:
                crop_size = (width - new_size)//2
                im = im.crop((crop_size,0,width-crop_size,height))
            else:
                crop_size = (height - new_size)//2
                im = im.crop((0,crop_size,width,height-crop_size))

            im.save(path)
            return


    def save(self, *args, **kwargs):
        # saving twice isnt ideal but cant get proper img path otherwise
        super().save(*args, **kwargs)
        self.crop_picture()
        super().save(*args, **kwargs)
        

    def __str__(self):
        return self.user.username


class Riddle(models.Model):
    # note there is an auto generated id field
    question = models.CharField(max_length=150)
    date_posted = models.DateField(auto_now_add=True)
    # easy: 0-50
    # medium: 51-100
    # hard: 101-150
    difficulty = models.IntegerField(default=75)
    rating = models.IntegerField(default=0)
    num_answers = models.IntegerField(default=0)

    author = models.ForeignKey(User, models.CASCADE)
    answered_by = models.ManyToManyField(UserProfile, through='UserAnswer')

    # Set of answers as comma seperated string
    answers = models.CharField(max_length=300, default="")

    def update_fields(self):
        useranswers = self.useranswer_set.all()

        self.num_answers = useranswers.count()

        # find average number of tries
        # incorrect answer == +10 tries
        total_tries = 0
        for ua in useranswers:
            total_tries += ua.num_tries
            if not ua.correct:
                total_tries += 10
        mean = total_tries / self.num_answers
        self.difficulty = mean * 20
        self.save()

    class Meta:
        verbose_name_plural = 'riddles'

    def __str__(self):
        return self.question


class UserAnswer(models.Model):
    user = models.ForeignKey(UserProfile, models.CASCADE)
    riddle = models.ForeignKey(Riddle, models.CASCADE)

    num_tries = models.IntegerField(default=0)
    correct = models.BooleanField(default=False)
    answer = models.CharField(max_length=30, default="")

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.riddle.update_fields()
