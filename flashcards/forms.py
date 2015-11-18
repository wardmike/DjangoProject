from django import forms

from .models import Flashcard
from .models import User

class FlashcardForm(forms.ModelForm):
	class Meta:
		model = Flashcard
		fields = ['spanish_word', 'english_word']

class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['user_name', 'email']

	def clean_email(self):
		email = self.cleaned_data.get('email')
		email_base, provider = email.split("@")
		domain, extension = provider.split(".")
		#Validation example:
		#if not extension == "edu":
		#	raise forms.ValidationError("Please use a valid .edu email address.")
		return email

	def clean_user_name(self):
		user_name = self.cleaned_data.get('user_name')
		#enter validation code here
		return user_name