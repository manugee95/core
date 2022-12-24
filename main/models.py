from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class HomeProfile(models.Model):
    appname = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='logo')
    carousel1 = models.ImageField(upload_to='carousel')
    carousel2 = models.ImageField(upload_to='carousel')
    carousel3 = models.ImageField(upload_to='carousel')
    carousel4 = models.ImageField(upload_to='carousel')
    carousel5 = models.ImageField(upload_to='carousel')
    carousel6 = models.ImageField(upload_to='carousel')
    carousel7 = models.ImageField(upload_to='carousel')
    carousel8 = models.ImageField(upload_to='carousel')
    aboutbanner = models.ImageField(upload_to='banner')
    servicebanner = models.ImageField(upload_to='banner')
    careerbanner = models.ImageField(upload_to='banner')
    abouttitle = models.CharField(max_length=200)
    abouttext = RichTextField()
    aboutimg = models.ImageField(upload_to='pix')
    phone = models.CharField(max_length=50)
    fax = models.CharField(max_length=50)
    email1 = models.EmailField(max_length=100)
    email2 = models.EmailField(max_length=100)

    def __str__(self):
        return self.appname
    
class Location(models.Model):
    state = models.CharField(max_length=100)
    description = RichTextField()

    def __str__(self):
        return self.state

class Service(models.Model):
    area = models.ForeignKey(Location, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    pix = models.ImageField(upload_to='pix')
    description = RichTextField()
    maryland = models.BooleanField()
    virginia = models.BooleanField()
    columbia = models.BooleanField()
    servicess = models.BooleanField()

    def __str__(self):
        return self.name

class State(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class StateApplied(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class PositionApplied(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Time(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Career(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip = models.CharField(max_length=10)
    cell_number = models.CharField(max_length=20)
    position_applied = models.CharField(max_length=50)
    state_applied = models.CharField(max_length=50)
    shift_applied_dc = models.CharField(max_length=20, blank=True, null=True)
    shift_applied_maryland = models.CharField(max_length=20, blank=True, null=True)
    shift_applied_virginia = models.CharField(max_length=20, blank=True, null=True)
    high_school_or_ged = models.CharField(max_length=20, blank=True, null=True)
    date_attended_from = models.CharField(max_length=20, blank=True, null=True)
    date_attended_to = models.CharField(max_length=20, blank=True, null=True)
    college_graduate = models.CharField(max_length=20, blank=True, null=True)
    college_graduate_from = models.CharField(max_length=20, blank=True, null=True)
    college_graduate_to = models.CharField(max_length=20, blank=True, null=True)
    eligible_in_the_us = models.CharField(max_length=20, blank=True, null=True)
    convicted = models.CharField(max_length=20, blank=True, null=True)
    convicted_explain = models.TextField(max_length=20, blank=True, null=True)
    violation = models.CharField(max_length=20, blank=True, null=True)
    violation_explain = models.TextField(max_length=20, blank=True, null=True)
    current_physical = models.CharField(max_length=20, blank=True, null=True)
    current_physical_upload = models.FileField(upload_to='physical')
    tbtest = models.CharField(max_length=20, blank=True, null=True)
    tbtest_upload = models.FileField(upload_to='tbtest')
    cpr_card = models.CharField(max_length=20, blank=True, null=True)
    cpr_card_upload = models.FileField(upload_to='cpr')
    first_aide_card = models.CharField(max_length=20, blank=True, null=True)
    first_aide_upload = models.FileField(upload_to='firstaide')
    resume = models.FileField(upload_to='resume')
    message = models.TextField()
    sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name