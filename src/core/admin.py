from django.contrib import admin
from .models import (MenuModel, TestimonialModel, GalleryModel, ChefModel, 
                     BookingModel, MenuCategory, SpecialModel, EventsModel, NewsletterModel)


class MenuAdmin(admin.ModelAdmin):
    list_display = ['category', 'name', 'image', 'description', 'price']


class Testimonialdmin(admin.ModelAdmin):
    list_display = ['name', 'image', 'message', 'occupation']


class ChefAdmin(admin.ModelAdmin):
    list_display = ['name', 'image', 'occupation']


class BookingAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'message','time', 'date']


class SpecialAdmin(admin.ModelAdmin):
    list_display = ['name', 'image', 'description']


class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'image', 'description', 'price']

class NewsletterAdmin(admin.ModelAdmin):
    list_display = ['email', 'date']





admin.site.register(MenuCategory)
admin.site.register(MenuModel, MenuAdmin)
admin.site.register(TestimonialModel, Testimonialdmin)
admin.site.register(GalleryModel)
admin.site.register(ChefModel, ChefAdmin)
admin.site.register(BookingModel, BookingAdmin)
admin.site.register(SpecialModel, SpecialAdmin)
admin.site.register(EventsModel, EventAdmin)
admin.site.register(NewsletterModel, NewsletterAdmin)






