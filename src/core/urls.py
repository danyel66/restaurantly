from django.urls import path
from .views import index, email_list_signup, contact, booking

urlpatterns = [
    path('', index, name='index'),
    path('subscribe/', email_list_signup, name='subscribe'),
    path('contact/', contact, name='contact'),
    path('booking/', booking, name='booking')

]