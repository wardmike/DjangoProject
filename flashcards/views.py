from django.conf import settings
from django.core.mail import send_mail
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
		form_email = form.cleaned_data.get("email")
		form_message = form.cleaned_data.get("message")
		form_full_name = form.cleaned_data.get("full_name")
		subject = 'Site Contact Form'
		from_email = settings.EMAIL_HOST_USER
		to_email = [from_email, form_email]
		contact_message = "%s: %s via %s" %(
			form_full_name,
			form_message,
			form_email)
		send_mail(subject, contact_message, from_email, to_email, fail_silently=False)
	context = {
		"form": form,
	}
	send_mail('Subject here', 'Here is the message.', 'from@example.com',
    ['to@example.com'], fail_silently=False)
	return render(request, "forms.html", context)