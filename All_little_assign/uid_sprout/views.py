from django.shortcuts import render, render_to_response
from django.template import loader, Context
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import django.conf.urls

# Create your views here.
def index(request):
	return render_to_response('index_uid.html',{})
