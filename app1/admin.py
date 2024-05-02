from django.contrib import admin
from app1.models import contactUs, report

# Register your models here.

class contactUsAdmin(admin.ModelAdmin):
    list_display = ('contactFullName', 'contactEmail', 'contactPhoneNumber', 'contactSubject', 'contactMessage')

admin.site.register(contactUs, contactUsAdmin)

class reportAdmin(admin.ModelAdmin):
    list_display = ('location', 'cause', 'damage', 'comments')

admin.site.register(report, reportAdmin)


    


