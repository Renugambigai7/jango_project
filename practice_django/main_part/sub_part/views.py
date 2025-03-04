from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . models import *


def index(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')

def dashboard(request):
    return render(request,'dashboard.html')

def product(request):
    return render(request,'product.html')
 
def customer(request):
    return render(request,'customer.html')

def register_form_submission(request):
   
    first_name=request.POST.get('first_name')
    last_name=request.POST.get('last_name')
    email_id=request.POST.get('email_id')
    password=request.POST.get('password')
    print(first_name,last_name,email_id,password)

    ex1=register_table(first_name=first_name,last_name=last_name,email_id=email_id,password=password)
    ex1.save()
    print("data are saved into database")
    return render(request,'register.html')
    
    
    
def login_form_submission(request):
    if register_table.objects.filter(email_id=request.POST.get('email_id'),password=request.POST.get('password')).exists():
        print("login success")
        logger_data=register_table.objects.get(email_id=request.POST.get('email_id'),password=request.POST.get('password'))
        return render(request,'dashboard.html',{'logger_data':logger_data})
    else:   
        print("login failed")
        return render(request,'login.html')
    





