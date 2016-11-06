"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from app.models import Artist

def all(request):
    
    """Renders a list of all Artists in the database."""
    assert isinstance(request, HttpRequest)
    title = "All Artists"
    year = datetime.now().year
    artist_list = Artist.objects.all()
    return render(
        request,
        "app/artists/list.html",
        context_instance = RequestContext(request,
        {
            "title":title,
            "year":year,
            "artist_list":artist_list
        })
    )


def artist_details(request, artist_id):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        "app/artists/artist_detail.html",
        RequestContext(request,
        {
            "title":"Artist Details",
            "year":datetime.now().year,
            "venue_details": Artist.objects.filter(id=artist_id)
        })
    )

#def artist_tours(request, artist_id):
#    from app.models import Tour
#    assert isinstance(request, HttpRequest)
#    artist = Artist.objects.filter(id=artist_id)
#    for tour in artist.
#    return render(
#        request,
#        "app/artists/artist_tours.html",
#        RequestContext(request,
#        {
#            "title":,
#            "year":datetime.now().year,
#            "artist": artist
#        })
#    )