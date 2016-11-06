from app.models import Venue
from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime

def venue_index(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        "app/venue/index.html",
        RequestContext(request,
        {
            "title":"Venues",
            "year":datetime.now().year,
        }
        )
    )

def all_venues(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        "app/venue/venue_list.html",
        RequestContext(request,
        {
            "title":"All Venues",
            "year":datetime.now().year,
            "venue_list": Venue.objects.filter()
        })
    )

def venue_details(request, venue_id):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        "app/venue/venue_detail.html",
        RequestContext(request,
        {
            "title":"Venue Details",
            "year":datetime.now().year,
            "venue_details": Venue.objects.filter(id=venue_id)
        })
    )

def venue_events(request, venue_id):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        "app/venue/venue_events.html",
        RequestContext(request,
        {
            "title":"Events at venue",
            "year":datetime.now().year,
            "event_list": Event.objects.filter(venue=venue_id)
        })
    )