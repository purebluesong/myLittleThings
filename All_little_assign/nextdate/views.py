from django.shortcuts import render, render_to_response
from django.template import loader, Context
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import django.conf.urls
from nextdate import Date_my, nextdate, getLunarValues, getWeekValues
# Create your views here.
def index(request):
	content = {}
	return render_to_response('index.html',content)

def compute(request):
	if request.method == "GET":
		print(request.GET.keys())
		year,month,day = request.GET['year'],request.GET['month'],request.GET['day']
	else:
		year,month,day = 1900,1,1
	date = nextdate(Date_my(int(year), int(month), int(day)))
	lunar_year,lunar_month,lunar_day = getLunarValues(date.lunar_year,date.lunar_month,date.lunar_day)
	week = getWeekValues(date.week)
	date_dict = {
		'year':date.year,
		'month':date.month,
		'day':date.day,
		'week':week,
		'lunar_year':lunar_year,
		'lunar_month':lunar_month,
		'lunar_day':lunar_day,
	}
	return JsonResponse(date_dict)
