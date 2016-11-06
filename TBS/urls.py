"""
Definition of urls for TBS.
"""

from datetime import datetime
from django.conf.urls import patterns, url
from app.forms import BootstrapAuthenticationForm
import app
# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()
import allauth

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'app.views.home', name='home'),
    url(r'^contact$', 'app.views.contact', name='contact'),
    url(r'^about', 'app.views.about', name='about'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # App Url's
    
    url(r'^artist/', include("app.artists.urls")),
    url(r'^event/', include("app.events.urls")),
    url(r'tour/', include("app.tours.urls")),
    url(r'^venue/', include("app.venue.urls")),
    url(r'^accounts/', include('allauth.urls')),


)
