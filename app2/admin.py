from django.contrib import admin

# Register your models here.

from app2.models import addRestaurentModel

class addRestaurentAdmin(admin.ModelAdmin):
    list_display = ('commpanyName', 'issuedBy', 'expiryDate', 'message')

admin.site.register(addRestaurentModel, addRestaurentAdmin)
