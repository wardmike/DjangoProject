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