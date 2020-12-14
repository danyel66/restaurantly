from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class MenuModel(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField()
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return self.name


class GalleryModel(models.Model):
    image_name = models.CharField(max_length=30)
    image = models.ImageField()

    def __str__(self):
        return self.image_name


class ChefModel(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField()
    twitter = models.URLField()
    facebook = models.URLField()
    instagram = models.URLField()
    linkedin = models.URLField()
    occupation = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class TestimonialModel(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField()
    occupation = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return self.name


class BookingModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = PhoneNumberField()
    date = models.DateField()
    time = models.TimeField()
    people = models.IntegerField()
    message = models.TextField()

    def __str__(self):
        return self.name
