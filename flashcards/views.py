from django.shortcuts import render

# Create your views here.
def home(request):
	if request.user.is_authenticated():
		title = "Welcome, %s!" %(request.user)
	else:
		title = "Welcome!"

	#add a form
	context = {
		"title": title,
	}
	return render(request, "home.html", context)