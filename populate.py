import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'riddlr_project.settings')

import django
django.setup()
from django.contrib.auth.models import User

from riddlr.models import Riddle, UserProfile


def populate():

    users = [
        {"username": "freddo",
         "score":20,
         "karma":4,
         "guess_ratio":1.2},
         {"username": "ginny",
         "score":3,
         "karma":-1,
         "guess_ratio":0.8},
         {"username": "rich",
         "score":43,
         "karma":35,
         "guess_ratio":3.448922},
         {"username": "xx_dumbledore_xx",
         "score":98,
         "karma":80,
         "guess_ratio":15.7424552},
         {"username": "lando",
         "score":2,
         "karma":0,
         "guess_ratio":-1},
         {"username": "blim",
         "score":0,
         "karma":0,
         "guess_ratio":None},
    ]

    riddles = [
        {"question": "What walks on four legs in the morning, 2 legs in the afternoon and 3 legs in the evening?",
         "answer_list": ["man", "a man", "a person", "a human"]},
        {"question": "I start with M and end with X. I have a never ending amount of letters. What am I?",
         "answer_list": ["a mailbox", "mailbox"]},
        {"question": "How many days in a week start with the letter T?",
         "answer_list": ["Four", "4"]},
    ]

# things break when users are added and i dont know why
    # for u in users:
    #     add_user(u["username"], u["score"], u["karma"], u["guess_ratio"])
    # print("Added "+str(len(users))+" users.")

    for r in riddles:
        add_riddle(r["question"], r["answer_list"])
    print("Added "+str(len(riddles))+" riddles.")

def add_user(username, score, karma, guess_ratio):
    u = User.objects.get_or_create(username=username)[0]
    u.save()
    up = UserProfile.objects.get_or_create(user=u, score=score, karma=karma, guess_ratio=guess_ratio)[0]
    up.save()


def add_riddle(question, answer_list):
    r = Riddle.objects.get_or_create(question=question)[0]
    r.set_answers(answer_list)
    r.save()


if __name__ == '__main__':
    print("Populating...")
    populate()
