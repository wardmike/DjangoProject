from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
	url(r'^$', 'flashcards.views.home', name="home"),
	url(r'^contact/', 'flashcards.views.contact', name="contact"),
    url(r'^admin/', include(admin.site.urls)),
]

