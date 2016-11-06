from datetime import datetime
from django.conf.urls import include, url
from app.forms import BootstrapAuthenticationForm
from app.views import *
from django.contrib.auth.views import login, logout

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r"^$", home, name="home"),
    url(r"^contact$", contact, name="contact"),
    url(r"^about", about, name="about"),
    url(r"^user/login/$",
        login,
        {
            "template_name": "app/login.html",
            "authentication_form": BootstrapAuthenticationForm,
            "extra_context":
            {
                "title":"Log in",
                "year":datetime.now().year,
            }
        },
        name="login"),
    url(r"^logout$",
        logout,
        {
            "next_page": "/",
        },
        name="logout"),


## Event"s

    url(r"^events/$", event_index, name="events"),
    url(r"^events/all", all_events, name="events"),
    url(r"^events/date/([0-9]{4})/$", event_year),
    url(r"^events/date/([0-9]{4})/([0-9]{2})/$", event_month),
    url(r"^events/date/([0-9]{4})/([0-9]{2})/([0-9]+)/$", event_day),
    ## Ensure that if date without trailing 0 is entered, we don't get a 404
    url(r"^events/date/([0-9]{4})/([0-9]{1})/$", event_month),
    url(r"^events/date/([0-9]{4})/([0-9]{1})/([0-9]+)/$", event_day),
    # url(r"^events/date/upcoming/$", "app.views.upcoming_events"),
    url(r"^events/detail/([0-9]{1})/$", event_details),

## Venue's
    url(r"^venues/$", venue_index, name="venues"),
    url(r"^venues/all", all_venues, name="venues"),
    url(r"^venues/detail/([0-9]{1})/$", venue_details),
    url(r"^venues/detail/([0-9]{1})/events/$", venue_events),
    
## User stuff

    url(r"^user/register/$", register, name="register"),


    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r"^admin/doc/", include("django.contrib.admindocs.urls")),

    # Uncomment the next line to enable the admin:
    url(r"^admin/", include(admin.site.urls)),
]
