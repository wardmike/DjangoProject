from django.db import models

# Create your models here.

class Flashcard(models.Model):
	english_word = models.CharField(max_length=20)
	spanish_word = models.CharField(max_length=20)

	def __unicode__(self): #__str__ for Python 3
		return self.spanish_word

class User(models.Model):
	email = models.EmailField(default='', blank=True, null=True)
	user_name = models.CharField(max_length=20)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	number_correct = models.IntegerField(default=0)
	number_incorrect = models.IntegerField(default=0)

	def __unicode__(self): #__str__ for Python 3
		return self.user_name