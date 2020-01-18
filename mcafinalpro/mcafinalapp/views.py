from __future__ import unicode_literals
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponse
from django.contrib.auth.models import User
from . models import Company
from .forms import CompanyFormmodel,StudentDataFormmodel
# Create your views here.
def LoginForm(request):
      return render(request,'home.html')
def rigistration(request):
      return render(request,'rigistration.html')
def user_saving(request):
      import pdb;pdb.set_trace()
      try:
        if request.method == "POST":
            first_name=request.POST.get('firstname')
            last_name=request.POST.get('secondname')
            email=request.POST.get('email')
            username = request.POST.get('username')
            password=request.POST.get('password')
            obj=User(username=username,first_name=first_name,last_name=last_name,email=email)
            obj.set_password(password)
            obj.save()
            return HttpResponseRedirect('loginpro/Login')
      except(ValueError):
            return HttpResponse("<html><body bgcolor=teal><h1>invalid</h1></body></html> ")
def Login(request):
    if request.method == "GET":
       return render(request,'home.html')
    elif request.method == "POST":
             #import pdb; pdb.set_trace()
            username=request.POST.get('username')    
            password=request.POST.get('password')
            if username and password is not None:
                  users=authenticate( username=request.POST.get('username'),password=request.POST.get('password'))
                  if users is not None:
                        users = User.objects.filter(username=username)
                        student_jobs = Company.objects.all()
                        return render(request,'userhunting.html',{'student_jobs':student_jobs,'users':users})
                  else:
                         return HttpResponse("<html><body bgcolor=teal><h1>invalid</h1></body></html>")
            else:
               return HttpResponse("<html><body bgcolor=teal><h1>invalid</h1></body></html>")
              
def CompanyRequrment(request):
  if request.method == "POST":
        forms = CompanyFormmodel(request.POST)
        if forms.is_valid():
            forms.save()
            return render(request,'requirment.html',{'forms':forms})
        else:
              return render(request,'requirment.html',{'forms':forms})
        
  forms = CompanyFormmodel()
  return render(request,'company.html',{'forms':forms})
def jobapply(request):
      import pdb;pdb.set_trace()
      print(request.GET)
      user_id = request.GET.get('user_id')
      company= request.GET.get('company_id')
      obj = User.objects.get(id=user_id)
      # if request.method == "POST":
      #        form = StudentDataFormmodel(request.POST)
      #        if form.is_valid():
      #            form.save()
      #            return render(request,'jobapply.html',{'form':form})
      #        else:
      #             return render(request,'jobapply.html',{'form':form})
      # form = StudentDataFormmodel()
      # # import pdb;pdb.set_trace()
      # # student_jobs = Company.objects.filter(id=comdata_id )
      # # print(student_jobs)
      # return render(request,'jobapply.html',{'form':form,})
      # adding code to git


