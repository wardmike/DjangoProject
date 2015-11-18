from django.shortcuts import render

from .forms import FlashcardForm
# Create your views here.
def home(request):
	if request.user.is_authenticated():
		title = "Welcome, %s!" %(request.user)
	else:
		title = "Welcome!"
	form = FlashcardForm(request.POST or None)
	message = ""
	#add a form
	# print request
	# if request.method == "POST":
	# 	print request.POST
	
	if form.is_valid():
		form.save() #saves directly to database
		instance = form.save(commit=False) #skips saving to allow stuff before
		spanish_word = form.cleaned_data.get("spanish_word")
		english_word = form.cleaned_data.get("english_word")
		instance.save() #saves into database
		print "added (%s, %s)" %(instance.spanish_word, instance.english_word)
		title = "Thank you!"
		message = "(%s, %s) added to database!" %(spanish_word, english_word)
	context = {
		"title": title,
		"form": form,
		"message": message,
	}
	
	return render(request, "home.html", context)