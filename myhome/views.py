from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from.models import Department, Doctors
from.forms import BookingForm

# class HomePageView(TemplateView):
#     template_name = "about.html"

# Create your views here.
def index (request):
    return render (request, 'index.html' )
def about (request):
    return render (request, 'about.html')
def booking (request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()    
        return render(request,'confirmation.html') #pointing to urls.py paths
    else:
            form = BookingForm()
    return render(request, "booking.html", {'form':form})
    # if request.method =='POST' in request.POST:
    #     form=BookingForm(request.POST)
    #     if form.is_Valid():
    #         form.save()

    # form=BookingForm()
    # dict_form={
    #     'form':form
    # }        
    # return render (request, 'booking.html',dict_form)
def doctors (request):
    dict_docs = {
        'doctors': Doctors.objects.all()
    }
    return render (request, 'doctors.html',dict_docs)
def contact (request):
    return render (request, 'contact.html')
def department (request):
    dict_dept ={
        'dept':Department.objects.all()
    }
    return render (request, 'department.html',dict_dept)    
