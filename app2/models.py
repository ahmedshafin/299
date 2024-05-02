from django.db import models

# Create your models here.

class addRestaurentModel(models.Model) :
    commpanyName = models.CharField(max_length=50)
    issuedBy = models.CharField(max_length=50)
    expiryDate = models.DateField()
    message = models.TextField()
