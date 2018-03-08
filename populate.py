import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'riddlr_project.settings')

import django
django.setup()
from riddlr.models import Riddle, User


def populate():
    riddles = [
        {"question": "What walks on four legs in the morning, 2 legs in the afternoon and 3 legs in the evening?",
         "answer_list": ["man", "a man", "a person", "a human"]},
        {"question": "I start with M and end with X. I have a never ending amount of letters. What am I?",
         "answer_list": ["a mailbox", "mailbox"]},
        {"question": "How many days in a week start with the letter T?",
         "answer_list": ["Four", "4"]},
    ]

    for r in riddles:
        add_riddle(r["question"],r["answer_list"])
    print("Added "+str(len(riddles))+" riddles.")


def add_riddle(question, answer_list):
    r = Riddle.objects.get_or_create(question=question)[0]
    r.set_answers(answer_list)
    r.save()

if __name__ == '__main__':
    print("Populating...")
    populate()