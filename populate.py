import os
import subprocess
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'riddlr_project.settings')

import django
django.setup()
from django.contrib.auth.models import User

from riddlr.models import Riddle, UserProfile


def populate():

    users = [
        {"username": "freddo",
         "score": 20,
         "karma": 4,
         "guess_ratio": 12},
        {"username": "ginny",
         "score": 3,
         "karma": -1,
         "guess_ratio": 8},
        {"username": "rich",
         "score": 43,
         "karma": 35,
         "guess_ratio": 3.448922},
        {"username": "xx_dumbledore_xx",
         "score": 98,
         "karma": 80,
         "guess_ratio": 75.7424552},
        {"username": "lando",
         "score": 2,
         "karma": 0,
         "guess_ratio": -1},
        {"username": "blim",
         "score": 0,
         "karma": 0,
         "guess_ratio": None},
    ]

    for u in users:
        add_user(u["username"], u["score"], u["karma"], u["guess_ratio"])
    print("Added "+str(len(users))+" users.")

    riddles = [
        {"question": "What walks on four legs in the morning, 2 legs in the afternoon and 3 legs in the evening?",
         "answer_list": ["man", "a man", "a person", "a human"],
         "author": User.objects.get(username="xx_dumbledore_xx"),
         "rating": 20},
        {"question": "I start with M and end with X. I have a never ending amount of letters. What am I?",
         "answer_list": ["a mailbox", "mailbox"],
         "author": User.objects.get(username="rich"),
         "rating": 5},
        {"question": "How many days in a week start with the letter T?",
         "answer_list": ["Four", "4"],
         "author": User.objects.get(username="xx_dumbledore_xx"),
         "rating": 2},
        {"question": "What has roots as nobody sees, is taller than trees, up, up it goes, and yet never grows?",
         "answer_list": ["a mountain", "mountain"],
         "author": User.objects.get(username="xx_dumbledore_xx"),
         "rating": 8},
        {"question": "If a tree falls in a forest and no one is there to hear it, does it make sound?",
         "answer_list": ["yes"],
         "author": User.objects.get(username="ginny"),
         "rating": -1},
        {"question": "A box without hinges, key, or lid, yet golden treasure inside is hid. What am I?",
         "answer_list": ["an egg", "egg"],
         "author": User.objects.get(username="rich"),
         "rating": 12},
    ]

    for r in riddles:
        add_riddle(r["question"], r["answer_list"], r["author"], r["rating"])
    print("Added "+str(len(riddles))+" riddles.")


def add_user(username, score, karma, guess_ratio):
    u = User.objects.get_or_create(username=username)[0]
    u.save()
    up = UserProfile.objects.get_or_create(user=u)[0]
    up.score = score
    up.karma = karma
    up.guess_ratio = guess_ratio
    up.save()


def add_riddle(question, answer_list, author, rating):
    r = Riddle.objects.get_or_create(
        question=question, author=author, rating=rating)[0]
    r.set_answers(answer_list)
    r.save()


if __name__ == '__main__':
    subprocess.call('ping 127.0.0.1', stdout=subprocess.PIPE)
    subprocess.call("python manage.py migrate --run-syncdb",
                    stdout=subprocess.PIPE)
    subprocess.call("python manage.py makemigrations", stdout=subprocess.PIPE)
    subprocess.call("python manage.py migrate", stdout=subprocess.PIPE)
    print("Populating...")
    populate()
