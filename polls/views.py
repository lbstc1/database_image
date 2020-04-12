from django.shortcuts import render
from django.http import HttpResponseRedirect
from.models import stu
from.forms import stu_form

def index(request):
    form=stu_form()
    if request.method=='POST':
        form=stu_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('about/')
    else:
        return render(request,'index.html',{'form':form})

def about(request):
    form=stu.objects.all()
    return render(request,'about.html',{'form':form})

def showdata(request):
    form=stu.objects.all()
    return render(request,'showdata.html',{'form':form})