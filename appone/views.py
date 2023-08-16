from django.shortcuts import render
from appone.forms import studentform
from appone.models import student
from django.http import HttpResponse
# Create your views here.

def liststudents(request):
    studentlist=student.objects.all()
    return render(request,'templates/d1.html',{'students':studentlist})

def addstudent(request):
    form=studentform()
    if request.method=='POST':
        form=studentform(request.POST)
        if form.is_valid():
            form.save()
    return  render(request, 'templates/d2.html',{'form':form})
