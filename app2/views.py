from django.shortcuts import render, redirect
from app2.models import addRestaurentModel
from app1.views import *
from app1.decorators import *

# Create your views here.


def dashboardView(request):
    return render(request, 'adminDashboard.html')

def addRestaurentView(request):
    if request.method =='POST' :
        companyName = request.POST.get('company')
        issue = request.POST.get('issuedBy')
        expiry = request.POST.get('expiryDate')
        message = request.POST.get('details')
        add = addRestaurentModel(commpanyName=companyName, issuedBy=issue, expiryDate=expiry, message=message)
        add.save()
        return redirect('dashboard')
    return render(request, 'addRestaurent.html')

