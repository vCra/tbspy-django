"""
Definition of urls for artists.
"""

from datetime import datetime
from django.conf.urls import patterns, url


urlpatterns = patterns('',
    url(r'^/', 'app.venue.views.venue_index', name='venue_index'),
    url(r'^all/', 'app.venue.views.all_venues', name='all_venues'),
    url(r'^details/(?P<venue_id>\d+)/$', 'app.venue.views.venue_details', name='venue_index'),
    url(r'^details/(?P<venue_id>\d+)/events/$', 'app.venue.views.venue_events', name='venue_events')
     
)
