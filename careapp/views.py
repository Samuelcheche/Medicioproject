from django.shortcuts import render,redirect,get_object_or_404
from careapp.models import *
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')

def starter(request):
    return render(request, 'starter-page.html')

def service_details(request):
    return render(request, 'service-details.html')

def about(request):
    return render(request, 'about.html')

def service(request):
    return render(request, 'service.html')


def department(request):
    return render(request, 'department.html')


def doctor(request):
    return render(request, 'doctor.html')


def contact(request):
    return render(request, 'contact.html')

def Appoint(request):
    if request.method == "POST":
       myappointment =Appointment(
                name= request.POST['name'],
                email= request.POST['email'],
                phone= request.POST['phone'],
                datetime= request.POST['datetime'],
                department= request.POST['department'],
                doctor= request.POST['doctor'],
                message= request.POST['message'],
        )
       myappointment.save()
       messages.success(request, 'Your appointment has been successfully booked!!!')
       return redirect('/appointment')
         
    else:
        return render(request, 'appointment.html')
        
    
def show(request):
    all =Appointment.objects.all()
    return render(request, 'show.html', {"all": all})

def delete(request,id):
    myappoint = Appointment.objects.get(id = id)
    myappoint.delete()
    messages.success(request, 'Your Appointment has been successfully deleted!!')
    return redirect('/show')

def edit(request,id):
    editappointment = get_object_or_404(Appointment, id = id)

    if request.method == "POST":
        editappointent.name = request.POST.get('name')
        editappointent.email = request.POST.get('email')
        editappointent.phone = request.POST.get('phone')
        editappointent.datetime = request.POST.get('date')
        editappointent.department = request.POST.get('department')
        editappointent.doctor = request.POST.get('doctor')
        editappointent.message = request.POST.get('message')

        editappointment.save()
        messages.success(request, 'Your appointment has been updated successfully!!')
        return render(request, 'edit.html')
    
    return render(request, 'edit.html', {'editappointment' : editappointment} )
