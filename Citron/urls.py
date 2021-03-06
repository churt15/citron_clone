"""Citron URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from Citron.views import HomePageView
from Citron.views import Aggregated_Map
from Citron.views import Sentiment_Data
from sentiments.views import postsJsonObject
from indicoio_theysay.views import indicoioSent

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^postsJsonObject/', postsJsonObject),
    url(r'^indicoio/', indicoioSent),
	url(r'^$', HomePageView.as_view(), name='home'),
	url('Aggregated_Map', Aggregated_Map.as_view(), name='map'),
	url('Sentiment_Data', Sentiment_Data.as_view(), name='sentiment')
]