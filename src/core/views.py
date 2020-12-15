from django.shortcuts import render, redirect
from django.contrib import messages
from .models import BookingModel, MenuModel, MenuCategory, GalleryModel, ChefModel, SpecialModel, TestimonialModel
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.core.mail import EmailMessage
from validate_email import validate_email


# def contact(request):
#     if request.method == 'GET':
#         form = ContactForm()
#     else:
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             subject = form.cleaned_data['Subject']
#             from_email = form.cleaned_data['Email']
#             message = form.cleaned_data['Message']
#             recipients = ['danison66@gmail.com',]
#             try:
#                 send_mail(subject, message, from_email, recipients, fail_silently=True)
#                 messages.success(request, 'Your Message was sent successfully.')
#             except BadHeaderError:
#                 messages.error(request, 'Invalid header found.')
#             return redirect('contact')
#     return render(request, 'core/index.html', {'form': form})


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

    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['Subject']
            email = form.cleaned_data['Email']
            message = form.cleaned_data['Message']
            recipients = ['danison66@gmail.com',]
            try:
                send_mail(subject, message, email, recipients, fail_silently=True)
                messages.success(request, 'Your Message was sent successfully.')
            except BadHeaderError:
                messages.error(request, 'Invalid header found.')
            return redirect('index')

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
        'form': form,
        'testimonial': testimonial
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

        if not validate_email(email):
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
        message = "Congration your reservation has been made for "+ people +' people on the '+ date +' and '+ time +' West African Time (WAT). We will be expecting you.'

        email = EmailMessage(
            subject,
            'Hi '+ name + ',' + '\n' + message,
            'noreply@semycolon.com',
            [email],
        )
        email.send(fail_silently=False)
        messages.success(request, 'Your Booking at Restaurantly has been saved successfully')
        return redirect('index')
    
    return render(request, 'core/index.html', context)


    

    