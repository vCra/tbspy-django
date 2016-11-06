"""
Definition of urls for artists.
"""

"""URLconf for Artists"""

from datetime import datetime
from django.conf.urls import patterns, url
from app.artists import views


urlpatterns = patterns('',
    url(r"^all", "app.artists.views.all", name="artists.all")
   
)