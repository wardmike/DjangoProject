from django.shortcuts import render

from .forms import ContactForm, FlashcardForm
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



def contact(request):
	form = ContactForm(request.POST or None)
	if form.is_valid():
		for key, value in form.cleaned_data.iteritems(): #iterating through values
			print key, value
			#print form.cleaned_data.get(key)
		#going through values individually:
		email = form.cleaned_data.get("email")
		message = form.cleaned_data.get("message")
		full_name = form.cleaned_data.get("full_name")
		print email, message, full_name
	context = {
		"form": form,
	}
	return render(request, "forms.html", context)