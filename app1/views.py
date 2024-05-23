import base64
import datetime
import os
from django.http import HttpResponseRedirect, HttpResponseBadRequest, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect, HttpResponse
from app1.models import contactUs as contactUsModel, report, addRestaurentModel, report, picture, TestUser, team, history,assignedTeam
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .decorators import unauthenticated_user, admin_only

# Create your views here.

def homeView(request) :
    return render(request, "home.html")



def viewHomepage(request) :
               
    return render(request, "index.html") 

#User signUp
def signUpView(request):
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
            return redirect('clickPicture')
        #User have been created
    return render(request, "signup.html")



#Admin Dashboard
def dashboardView(request):
    
    reports = report.objects.filter()
    report_count= len(reports)
    all_users = User.objects.all()
    user_count = len(all_users)
    all_certificates = addRestaurentModel.objects.filter()
    certificates_count = len(all_certificates)
    restaurents = addRestaurentModel.objects.filter()
    notification = contactUsModel.objects.filter()
    notification_count = len(notification)
    availableTeam = team.objects.filter()
    
    args = {
        "reports": reports,
        "report_count":report_count,
        "user_count":user_count,
        "certificates_count":certificates_count,
        "restaurents":restaurents,
        "notification_count":notification_count,
        "availableTeam":availableTeam

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
        elif loginName == "team":
            if user is not None :
                login(request, user)
                return redirect('team')
        else:   
            if user is not None :
                login(request, user)
                return redirect('faceRecog')
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

#Contact Display
def clickPicture(request):
    last_object =User.objects.latest('id') 
    last_object_user=last_object.username
    
    if request.method=="POST":
        img=request.POST.get("img_data")
        picture_obj = picture.objects.create(
            userName=last_object_user,
            img=img
        )
        picture_obj.save()
        return redirect('home')
           
    return render(request, "face.html")

#GPS Tracking
def map(request, slug):
    map_obj = get_object_or_404(report, id=slug)
    latitude = map_obj.latitude
    longitude = map_obj.longitude
    google_maps_url = f"https://www.google.com/maps?q={latitude},{longitude}"

        # Appending the search query for nearby lakes to the Google Maps URL
    google_maps_url += "&q=nearby river"
    return redirect(google_maps_url)

#GPS Tracking
def map2(request, slug):
    map_obj = get_object_or_404(assignedTeam, id=slug)
    latitude = map_obj.latitude
    longitude = map_obj.longitude
    google_maps_url = f"https://www.google.com/maps?q={latitude},{longitude}"

        # Appending the search query for nearby lakes to the Google Maps URL
    google_maps_url += "&q=nearby river"
    return redirect(google_maps_url)
    
def deleteContact(request, slug):
    certificate = contactUsModel.objects.get(id=slug)
    certificate.delete()

        # Appending the search query for nearby lakes to the Google Maps URL
    
    return redirect('displayContact')


#Face Recognition Verification
def faceRecog(request):
    if request.method=="POST":
          
    
        return redirect(f"/check/")
    return render(request,'faceRecog.html')

def check(request):
   
    db = picture.objects.get(userName=request.user)
    db_img=db.img
    dbu=db.userName
    temp = str(request.user)
   
    
    db1 = TestUser.objects.get(user=temp)
    db_img1=db1.img
    dbu1=db1.user
    
    if dbu == dbu1 and db_img == db_img1:
        
        return redirect(f"/home/")
    else:
        return HttpResponse("Access Denied. Face didnt match")   


#Available Teams
def addTeam(request):
    if request.method == 'POST':
        teamName = request.POST.get('name')  # Get the team name from the form
        # Create a new Team instance and save it to the database
        
        newTeam = team(name=teamName)

        newTeam.save()
        return redirect('addTeam')
    
    return render(request, 'availableteam.html', {'teams': team.objects.all()}) 


#Delete Team
def deleteTeam(request, slug):
    delTeam = team.objects.get(id=slug)
    delTeam.delete()

    return redirect('addTeam')


#Delete Certificate
def deleteCertificate(request, slug):
    delCertificate = addRestaurentModel.objects.get(id=slug)
    delCertificate.delete()

    return redirect('dashboardView')


#Search Bar
def searchReports(request):
    if request.method == 'POST':
        location_query = request.POST.get('q')
        # Search for reports based on the provided location
        reports = report.objects.filter(location__icontains=location_query)
        return render(request, 'search_results.html', {'reports': reports})
    else:
        return render(request, 'search_form.html')
    

#Resolving and Backlog
#assigning the work to the teams
def resolve(request, slug):
    delReport = report.objects.get(id=slug)
    if request.method == 'POST':
        teamName = request.POST.get('teamName')
        assigned = 1
        teams = assignedTeam(name=teamName, assigned=assigned, location=delReport.location,cause=delReport.cause,damage=delReport.damage,comments=
                             delReport.comments,latitude=delReport.latitude,longitude=delReport.longitude)
        teams.save()
    
    
    
    
    delTeam = team.objects.get(name=teamName)
    
    delTeam.delete()
    
    delReport.delete()
    
    return redirect('dashboardView')

def log(request):
    log = history.objects.all()
    
    return render(request, 'log.html',{'log': log})


#Team Completion
def teamLogin(request):

    teams = assignedTeam.objects.filter()

    args = {
        'teams': teams,
        
    }
    return render(request, 'team.html',args)

def teamUpdate(request,slug):
    print(slug)
    teams = assignedTeam.objects.get(id=slug)
    if request.method == 'POST':
        new_text = request.POST.get('my_text_area')
        
        teams.complete = new_text
        teams.save()
    
    current_date = datetime.date.today()
    current_time = datetime.datetime.now().time()
    log = f"Date: {current_date}, Time: {current_time}, Team name: {teams.name}, solved the case report ID: {teams.id}, location: {teams.location} Comments: {teams.complete} WORK DONE"
    history_entry = history(log=log)
    history_entry.save()

    teams.delete()
    return redirect(teamLogin)





    
    

        
       
