from django.db import models
from django.contrib.auth.models import User
from allauth.account.models import EmailAddress
# Create your models here.

class Artist(models.Model):
    name = models.CharField(max_length=80)
    details = models.TextField(blank = True, null=True)
    website = models.URLField(blank = True, null=True)
    #image = models.ImageField(upload_to="artist_images",blank = True, null=True)
    featured = models.BooleanField(blank = True)

    def __str__(self):
        return self.name

class Venue(models.Model):
    name = models.CharField(max_length=100)
    details = models.TextField(blank = True, null=True)
    address1 = models.CharField(max_length=30,blank = True, null=True)
    address2 = models.CharField(max_length=30, blank = True, null=True)
    address3 = models.CharField(max_length=30, blank = True, null=True)
    town = models.CharField(max_length=30, blank = True, null=True)
    postcode = models.CharField(max_length=10, blank = True, null=True)
    website = models.URLField(blank = True, null=True)
    #image = models.ImageField(upload_to="venue_images",blank = True, null=True
    phone = models.IntegerField(max_length=11,blank = True, null=True)
    total_seats = models.IntegerField()
    featured = models.BooleanField(blank = True)

    def __str__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=100)
    details = models.TextField(blank = True, null=True)
    artists = models.ManyToManyField(Artist,blank = True, null=True)
    date = models.DateTimeField()
    finish_time = models.TimeField()
    total_seats = models.IntegerField()
    venue = models.ForeignKey(Venue)
    website = models.URLField(blank = True, null=True)
    #image = models.ImageField(upload_to="event_images",blank = True, null=True)
    featured = models.BooleanField(blank = True)
    def __str__(self):
        return self.name

    def seats_free(self):
        return self.total_seats - self.seats_taken


class Price(models.Model):
    name = models.CharField(max_length=30)
    event = models.ForeignKey(Event)
    notes = models.CharField(max_length=100, blank = True, null=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    def __str__(self):
        return (self.event.name +" - " + self.name)

class Ticket(models.Model):
    Owner = models.ForeignKey(User)
    Event = models.ForeignKey(Event)
    Price = models.ForeignKey(Price)
    def __str__(self):
        return str(self.pk)

class Tour(models.Model):
    name = models.CharField(max_length=80)
    details = models.TextField(blank = True, null=True)
    events = models.ManyToManyField(Event,blank = True, null=True)
    def __str__(self):
        return str(self.name)

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile')
    tickets = models.ManyToManyField(Ticket,blank = True, null=True)
    DOB = models.DateField()
    age = models.IntegerField()
    def __unicode__(self):
        return "{}'s profile".format(self.user.username)
 
    class Meta:
        db_table = 'user_profile'
 
    def account_verified(self):
        if self.user.is_authenticated:
            result = EmailAddress.objects.filter(email=self.user.email)
            if len(result):
                return result[0].verified
        return False

    @property
    def age(self):
        birthdate = self.DOB
        from datetime import date
        if (date.today() - birthdate.replace(year=date.today().year)).days >= 0:
            age = years
        else:
            age = years - 1

 
User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])

