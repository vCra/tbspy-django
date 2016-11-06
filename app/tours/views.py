"""Views for Tours"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from app.models import Tour, Event

def all(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        "app/tours/list.html",
        RequestContext(request,
        {
            "title":"All Tours",
            "year":datetime.now().year,
            "tour_list": Tour.objects.all()
        })
    )

def byArtist(request, artist):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        "app/tours/list.html",
        RequestContext(request,
        {
            "title":{"All Tours by", artist},
            "year":datetime.now().year,
            "tour_list": Tour.objects.filter(Artists=artist)
        })
    )

def details(request, tour_id):
    assert isinstance(request, HttpRequest)

    title = "Tour"
    year = datetime.now().year
    tourObject = Tour.objects.filter(id=tour_id)
    tourObjectEvents

    return render(
        request,
        "app/tours/tours_detail.html",
        RequestContext(request,
        {
            "title":title, 
            "year":year,
            "tourObject": tourObject,
            "tourObjectEvents": tourObjectEvents,
        })
    )