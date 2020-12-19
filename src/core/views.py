from django.shortcuts import render, redirect
from django.contrib import messages
from .models import (BookingModel, MenuModel, MenuCategory, GalleryModel, 
                        ChefModel, SpecialModel, TestimonialModel, EventsModel, NewsletterModel)
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.core.mail import EmailMessage
from django.conf import settings
import json
from .forms import NewsletterForm
from django.http import HttpResponseRedirect
import requests
from validate_email import validate_email

MAILCHIMP_API_KEY = settings.MAILCHIMP_API_KEY
MAILCHIMP_DATA_CENTER = settings.MAILCHIMP_DATA_CENTER
MAILCHIMP_EMAIL_LIST_ID = settings.MAILCHIMP_EMAIL_LIST_ID


api_url = f'https://{MAILCHIMP_DATA_CENTER}.api.mailchimp.com/3.0'
members_endpoint = f'{api_url}/lists/{MAILCHIMP_EMAIL_LIST_ID}/members'

def subscribe(email):
    data = {
    "email_address": email,
    "status": "subscribed",
  }

    r = requests.post(
        members_endpoint,
        auth=('', MAILCHIMP_API_KEY),
        data = json.dumps(data)
    )
    return r.status_code, r.json()


def email_list_signup(request):
    form = NewsletterForm(request.POST)
    
    if request.method == 'POST':
            if form.is_valid():
                email_list_qs = NewsletterModel.objects.filter(email=form.instance.email)

                if email_list_qs.exists():
                    messages.error(request, "You are already subscribed to our Newsletter")

                else:
                    subscribe(form.instance.email)
                    form.save()
                    messages.success(request, "Congratulation!! you've successfully subscribed to our Newsletter")

        
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    
def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['Subject']
            from_email = form.cleaned_data['Email']
            message = form.cleaned_data['Message']
            recipients = ['danison66@gmail.com',]
            try:
                send_mail(subject, message, from_email, recipients, fail_silently=True)
                messages.success(request, 'Your Message was sent successfully.')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            except BadHeaderError:
                messages.error(request, 'Invalid header found.')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return render(request, 'core/index.html', {'form': form})


def booking(request):
    context = {
        'value': request.POST,
    }

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        date = request.POST['date']
        time = request.POST['time']
        people = request.POST['people']
        message = request.POST['message']

        if not name:
            messages.error(request, 'Name is required')
            return render(request, 'core/index.html', context)

        if not validate_email(email, check_mx=True, verify=True, debug=True):
            messages.error(request, 'Input a correct Email', )
            return render(request, 'core/index.html', context)
        
        if not phone:
            messages.error(request, 'Phone Number is required')
            return render(request, 'core/index.html', context)

        if not date:
            messages.error(request, 'Date Field is required')
            return render(request, 'core/index.html', context)

        if not time:
            messages.error(request, 'Time is required')
            return render(request, 'core/index.html', context)
        
        if not people:
            messages.error(request, 'Number of guests is required')
            return render(request, 'core/index.html', context)

        if not message:
            messages.error(request, 'Message is required')
            return render(request, 'core/index.html', context)


        BookingModel.objects.create(name=name, email=email, phone=phone, date=date, time=time,
                                    people=people, message=message)

        subject = 'Table Booking Email'
        message = "Congratulation, your reservation has been made for "+ people +' people on the '+ date +' and '+ time +' West African Time (WAT). We will be expecting you.'

        email = EmailMessage(
            subject,
            'Hi '+ name + ',' + '\n' + message,
            'noreply@semycolon.com',
            [email],
        )
        email.send(fail_silently=False)
        messages.success(request, 'Your Booking at Restaurantly has been saved successfully')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))



def index(request):
    category = MenuCategory.objects.all()
    all_items = MenuModel.objects.all()[:10]
    appetizers = MenuModel.objects.filter(category_id=1)[:6]
    comfort_food = MenuModel.objects.filter(category_id=2)[:6]
    desserts = MenuModel.objects.filter(category_id=6)[:6]
    kid_menu_item = MenuModel.objects.filter(category_id=5)[:6]
    pizza = MenuModel.objects.filter(category_id=4)[:6]
    gallery = GalleryModel.objects.all()[:8]
    chef = ChefModel.objects.all()[:3]
    specials = SpecialModel.objects.all()[:5]
    testimonial = TestimonialModel.objects.all()[:6]
    events = EventsModel.objects.all()

    news_form = NewsletterForm()
    contact_form = ContactForm()

    context = {
        'all_items': all_items,
        'appetizers': appetizers,
        'comfort_food': comfort_food,
        'desserts': desserts,
        'kid_menu_item': kid_menu_item,
        'pizza': pizza,
        'category': category,
        'gallery': gallery,
        'chefs': chef,
        'specials': specials,
        'value': request.POST,
        'contact_form': contact_form,
        'testimonial': testimonial,
        'events': events,
        'news_form': news_form
    }

   
    
    return render(request, 'core/index.html', context)


    

    