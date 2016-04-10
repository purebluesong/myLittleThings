from django.shortcuts import render, render_to_response
from django.template import loader, Context
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import django.conf.urls
import models

# Create your views here.
def index(request):
	return render_to_response('index_uid.html',{})

def regeister(request):
	regSuccess = False
	reason = "name,email or password does'nt exist"+str(request.GET.keys())
	if set(['name','email','pwd']) == set(request.GET.keys()):
		username = request.GET['name']
		email = request.GET['email']
		password = request.GET['pwd']
		reason = "the username has been used"
		if not models.User.objects.filter(name=username):
			try:
				user = models.User(name=username, email=email, password=password)
				user.save()
				reason=""
				regSuccess = True
			except Exception, e:
				raise e
	return 	JsonResponse({'success':regSuccess,'reason':reason})