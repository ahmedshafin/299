from django.db import models

# Create your models here.

class contactUs(models.Model) :
    contactFullName = models.CharField(max_length=50)
    contactEmail = models.CharField(max_length=50)
    contactPhoneNumber = models.IntegerField()
    contactSubject = models.CharField(max_length=50)
    contactMessage = models.TextField()


class report(models.Model) :
    location = models.CharField(max_length=50)
    cause = models.CharField(max_length=50)
    damage = models.CharField(max_length=50)
    comments = models.TextField()







