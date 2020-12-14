from django.shortcuts import render, redirect
from django.contrib import messages
from .models import BookingModel


def index(request):


    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        date = request.POST['date']
        time = request.POST['time']
        people = request.POST['people']
        message = request.POST['message']


        BookingModel.objects.create(name=name, email=email, phone=phone, date=date, time=time,
                                    people=people, message=message)
        messages.success(request, 'Your Booking at Restaurantly has been saved successfully')

        return redirect('index')
    context = {

    }
    return render(request, 'core/index.html', context)


def bookingForm(request):
    pass

    