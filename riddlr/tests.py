from django.test import TestCase
from riddlr.models import Riddle, UserProfile
from django.contrib.auth.models import User
# Create your tests here.




class CreateRiddle(TestCase):
	def test_for_user_creation(self):
		u=User.objects.get_or_create(username="fred")
		Up = UserProfile.objects.get_or_create(user=u)
		Up.save()
		self.assertEqual((Up.karma==0), true)

	def test_to_ensure_rating_is_zero(self):
		u=User.objects.get_or_create(username="fred")
		Up = UserProfile.objects.get_or_create(user=u)
		Up.save()
		riddle = Riddle(question='How many are you', answers='two',author=Up)
		riddle.save()
		self.assertEqual((riddle.rating == 0), true)