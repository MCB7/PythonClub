from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# Create your models here.
class Meeting(models.Model):
    meetingtitle=models.CharField(max_length=255)
    meetingdate=models.DateField()
    meetingtime=models.DateTimeField()
    location=models.CharField(max_length=255)
    agenda=models.TextField()

    def __str__(self):
        return self.meetingtitle
    
    class Meta:
        db_table='meeting'

class MeetingMinute(models.Model):
    meetingid=models.ForeignKey(Meeting, on_delete=models.CASCADE)
    meetingattendance=models.ManyToManyField(User)
    meetingminutes=models.TextField()

    def __int__(self):
        return self.meetingid

    class Meta:
        db_table='meetingminute'

class Resource(models.Model):
    resourcename=models.CharField(max_length=255)
    resourcetype=models.CharField(max_length=255)
    url=models.URLField()
    dateentered=models.DateField()
    userid=models.ForeignKey(User, on_delete=models.CASCADE)
    description=models.TextField()

    def __str__(self):
        return self.resourcename

    class Meta:
        db_table='resource'

class Event(models.Model):
    title=models.CharField(max_length=255)
    location=models.CharField(max_length=255)
    date=models.DateField()
    time=models.DateTimeField()
    description=models.TextField()
    userid=models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        db_table='event'
