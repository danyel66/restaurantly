from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class MenuCategory(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class MenuModel(models.Model):
    category = models.ForeignKey(MenuCategory, related_name='Menu', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='menu_images/%Y/%m/%d' )
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10)


    class Meta:
        ordering = ('name',)
        verbose_name = 'menu item'
        verbose_name_plural = 'menu items'

    def __str__(self):
        return self.name


class GalleryModel(models.Model):
    image_name = models.CharField(max_length=30)
    image = models.ImageField()


    class Meta:
        ordering = ('image_name',)
        verbose_name = 'image gallery'
        verbose_name_plural = 'image gallery'

    def __str__(self):
        return self.image_name


class ChefModel(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='chef/%Y/%m/%d', )
    twitter = models.URLField()
    facebook = models.URLField()
    instagram = models.URLField()
    linkedin = models.URLField()
    occupation = models.CharField(max_length=200)


    class Meta:
        ordering = ('name',)
        verbose_name = 'chef'
        verbose_name_plural = 'chefs'

    def __str__(self):
        return self.name


class TestimonialModel(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='testimonials/%Y/%m/%d', )
    occupation = models.CharField(max_length=50)
    message = models.TextField()

    class Meta:
        ordering = ('name',)
        verbose_name = 'testimonial'
        verbose_name_plural = 'testimonials'

    def __str__(self):
        return self.name


class SpecialModel(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='specials/%Y/%m/%d',)
    description = models.TextField()

    class Meta:
        ordering = ('name',)
        verbose_name = 'special offer'
        verbose_name_plural = 'special offers'

    def __str__(self):
        return self.name


class EventsModel(models.Model):
    title = models.CharField(max_length=30)
    image = models.ImageField(upload_to='events/%Y/%m/%d')
    price = models.IntegerField()
    description = models.TextField()

    class Meta:
        ordering = ('title',)
        verbose_name = 'Event'

    def __str__(self):
        return self.title

class BookingModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = PhoneNumberField()
    date = models.DateField()
    time = models.TimeField()
    people = models.IntegerField()
    message = models.TextField()

    class Meta:
        ordering: ['-date']
        verbose_name = 'Table Booking'
        verbose_name_plural = 'Table Bookings'


    def __str__(self):
        return self.name

class NewsletterModel(models.Model):
    email = models.EmailField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering: ['-date']
        verbose_name = 'Newletter'


    def __str__(self):
        return self.email
