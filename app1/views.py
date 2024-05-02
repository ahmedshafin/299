from django.shortcuts import render, redirect, HttpResponse
from app1.models import contactUs as contactUsModel, report
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .decorators import unauthenticated_user, admin_only

# Create your views here.

def homeView(request) :
    return render(request, "home.html")



def viewHomepage(request) :
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
                 
    return render(request, "index.html") 



def loginView(request) :
    if  request.method == 'POST' :
        loginName = request.POST.get('logName')
        loginPass = request.POST.get('logPass')
        print(loginName, loginPass)
        user = authenticate(request,username = loginName, password = loginPass )
        if user is not None :
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("Username or Password is incorrect") 
        
    return render(request, "index.html")     

  

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


def reportView(request) :
    if request.method =='POST' :
        locate = request.POST.get('location')
        reason = request.POST.get('cause')
        extentDamage = request.POST.get('damage')
        description = request.POST.get('comments')
        print(locate, reason, extentDamage, description)
        rep = report(location=locate, cause=reason, damage=extentDamage, comments=description)
        rep.save()
        return redirect('home')
    
    return render(request, "report.html")

def aboutView(request) :
    return render(request, "about.html")


def safetyView(request) :
    return render(request, "safety.html")

def certificateView(request) :
    return render(request, "certificate.html")



    

