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


    def update_fields(self):
        useranswers = self.useranswer_set.all()

        self.score = 0
        for ua in useranswers:
            points = 0
            if ua.correct:
                if ua.num_tries == 1:
                    points = 10
                elif ua.num_tries <=3:
                    points = 5
                else:
                    points = 1
            if ua.riddle.difficulty_pt == "hard":
                points *= 3
            elif ua.riddle.difficulty_pt == "medium":
                points *= 2
            self.score += points

        total = 0
        for r in self.riddle_set.all():
            total += r.rating
        self.karma = total
        
        total_num_tries = 0
        for ua in useranswers:
            total_num_tries += ua.num_tries

        if total_num_tries > 0:
            self.guess_ratio = (useranswers.filter(correct=True).count() / total_num_tries)*100


    def save(self, *args, **kwargs):
        # saving twice isnt ideal but cant get proper img path otherwise
        super().save(*args, **kwargs)
        self.update_fields()
        self.crop_picture()
        super().save(*args, **kwargs)
        

    def __str__(self):
        return self.user.username


class Riddle(models.Model):
    # note there is an auto generated id field
    question = models.CharField(max_length=400)
    date_posted = models.DateField(auto_now_add=True)
    # easy: 0-50
    # medium: 51-100
    # hard: 101-150
    difficulty = models.IntegerField(default=75)
    difficulty_pt = models.CharField(max_length=10,default="medium")
    rating = models.IntegerField(default=0)
    num_answers = models.IntegerField(default=0)

    author = models.ForeignKey(User, models.CASCADE)
    answered_by = models.ManyToManyField(UserProfile, through='UserAnswer')

    # Set of answers as comma seperated string
    answers = models.CharField(max_length=300, default="")

    def update_fields(self):
        useranswers = self.useranswer_set.all()

        self.num_answers = useranswers.count()

        total = 0
        for ua in useranswers:
            total += ua.rating
        self.rating = total

        # find average number of tries
        # incorrect answer == +10 tries
        total_tries = 0
        for ua in useranswers:
            total_tries += ua.num_tries
            if not ua.correct:
                total_tries += 10
        if self.num_answers >0 :
            mean = total_tries / self.num_answers
            self.difficulty = mean * 20

        if self.difficulty < 50:
            self.difficulty_pt = "easy"
        elif self.difficulty >= 50 and self.difficulty < 100:
            self.difficulty_pt = "medium"
        else:
            self.difficulty_pt = "hard"


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.update_fields()
        super().save(*args, **kwargs)

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

    # is either 1 or -1
    rating = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.riddle.save()
        self.user.save()
