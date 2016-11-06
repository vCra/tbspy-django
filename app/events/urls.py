"""
Definition of urls for artists.
"""

from datetime import datetime
from django.conf.urls import patterns, url


urlpatterns = patterns('',
    url(r'^contact$', 'app.views.contact', name='contact')
   
)
