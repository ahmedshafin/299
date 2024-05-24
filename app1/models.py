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
    latitude = models.FloatField()
    longitude = models.FloatField()
    
class addRestaurentModel(models.Model) :
    commpanyName = models.CharField(max_length=50)
    issuedBy = models.CharField(max_length=50)
    expiryDate = models.DateField()
    message = models.TextField()
    
class picture(models.Model):
    userName = models.TextField()
    img = models.TextField()


class TestUser(models.Model):
    user=models.TextField()
    img= models.TextField()

class team(models.Model):
    name = models.CharField(max_length=100)
    
class assignedTeam(models.Model):
    name = models.CharField(max_length=100)
    assigned = models.IntegerField(default=0)
    location = models.CharField(max_length=50, null=True)
    cause = models.CharField(max_length=50, null=True)
    damage = models.CharField(max_length=50, null=True)
    comments = models.TextField( null=True)
    latitude = models.FloatField( null=True)
    longitude = models.FloatField( null=True)
    complete = models.CharField(max_length=200, null=True)
    
    
class history(models.Model):
    log = models.CharField(max_length=500)


class emergencyReport(models.Model) :
    location = models.CharField(max_length=50)
    phoneNumber = models.IntegerField()
    comments = models.TextField()
    




