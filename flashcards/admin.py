from django.contrib import admin

# Register your models here.
from .forms import FlashcardForm
from .forms import UserForm
from .models import User
from .models import Flashcard

class FlashcardAdmin(admin.ModelAdmin):
	list_display = ["spanish_word", "english_word"]
	form = FlashcardForm
	#class Meta:
	#	model = Flashcard

class UserAdmin(admin.ModelAdmin):
	form = UserForm

admin.site.register(User, UserAdmin)
admin.site.register(Flashcard, FlashcardAdmin)