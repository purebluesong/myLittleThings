from django.conf.urls import include, url
import views

urlpatterns = [
	url(r'^$',views.index),
	url(r'^reg$',views.regeister),
]