from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect, HttpResponse
from app1.models import contactUs as contactUsModel, report, addRestaurentModel, report
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .decorators import unauthenticated_user, admin_only

# Create your views here.

def homeView(request) :
    return render(request, "home.html")



def viewHomepage(request) :
    #Create user code
    if  request.method =='POST': 
        userName = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('pass1')
        confirmPassword = request.POST.get('pass2')
        if password != confirmPassword:
            return HttpResponse("Your password and confirm password doesn't match")
        else:    
            myUser = User.objects.create_user(userName, email, password)
            myUser.save()
            return redirect('homepage')
        #User have been created           
    return render(request, "index.html") 


#Admin Dashboard
def dashboardView(request):
    reports = report.objects.filter()
    report_count= len(reports)
    all_users = User.objects.all()
    user_count = len(all_users)
    all_certificates = addRestaurentModel.objects.filter()
    certificates_count = len(all_certificates)
    args = {
        "reports": reports,
        "report_count":report_count,
        "user_count":user_count,
        "certificates_count":certificates_count
    }
    return render(request, 'adminDashboard.html', args)


#User Authentication
def loginView(request) :
    if  request.method == 'POST' :
        loginName = request.POST.get('logName')
        loginPass = request.POST.get('logPass')
        
        user = authenticate(request,username = loginName, password = loginPass )
        if loginName == "admin":
            if user is not None :
                login(request, user)
                return redirect('dashboardView')
            else:
                return HttpResponse("Username or Password is incorrect")  
        else:   
            if user is not None :
                login(request, user)
                return redirect('home')
            else:
                return HttpResponse("Username or Password is incorrect") 
        
    return render(request, "index.html")     

  
#Contact Us Page
def contactUs(request) : 
    if request.method =='POST' :
        fullName = request.POST.get('full_name')
        email = request.POST.get('email')
        phoneNumber = request.POST.get('phone_number')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        en = contactUsModel(contactFullName=fullName, contactEmail=email, contactPhoneNumber=phoneNumber, contactSubject=subject, contactMessage=message)
        en.save()
        return redirect('homepage')
        
    return render(request, "contact.html")


#User Report
def reportView(request) :
    if request.method =='POST' :
        locate = request.POST.get('location')
        reason = request.POST.get('cause')
        extentDamage = request.POST.get('damage')
        description = request.POST.get('comments')
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        
        # Do something with latitude and longitude  
        rep = report(location=locate, cause=reason, damage=extentDamage, comments=description, latitude=latitude,
          longitude=longitude)
        rep.save()
        return redirect('home')
    
    return render(request, "report.html")


def aboutView(request) :
    return render(request, "about.html")


def safetyView(request) :
    return render(request, "safety.html")


#Adding Certification to User
def certificateView(request):
    restaurants = addRestaurentModel.objects.filter()
    args = {
        "restaurants": restaurants,  
    }
    return render(request, "certificate.html", args)


#Adding Certification from Admin 
def addRestaurentView(request):
    if request.method =='POST' :
        companyName = request.POST.get('company')
        issue = request.POST.get('issuedBy')
        expiry = request.POST.get('expiryDate')
        message = request.POST.get('details')
        add = addRestaurentModel(commpanyName=companyName, issuedBy=issue, expiryDate=expiry, message=message)
        add.save()
        return redirect('dashboardView')
    return render(request, 'addRestaurent.html')


#Contact Display
def displayContactView(request):
    contacts = contactUsModel.objects.filter()
    
    args = {
        "contacts": contacts,  
    }
    return render(request, "contactAdmin.html",args)


#GPS Tracking
def map(request, slug):
    map_obj = get_object_or_404(report, id=slug)
    latitude = map_obj.latitude
    longitude = map_obj.longitude
    google_maps_url = f"https://www.google.com/maps?q={latitude},{longitude}"

        # Appending the search query for nearby lakes to the Google Maps URL
    google_maps_url += "&q=nearby river"
    return redirect(google_maps_url)
    
    




    

