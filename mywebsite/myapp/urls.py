from django.conf.urls import include, url
from django.contrib import admin
from myapp.feeds import LatestEntriesFeed
from myapp import views


urlpatterns = [
	
	url(r'^signup/upload$', views.upload,name="upload"),
    url(r'^signup/jh', views.nk,name="nk"),
     
]
    
