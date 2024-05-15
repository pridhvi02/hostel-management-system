from email.policy import default
from django.db import models

# Create your models here.

# class Topic(models.Model):
#     top_name = models.CharField(max_length=255 , unique=True)

# def __str__(self):
#     return self.top_name

# class Webpage(models.Model):
#     topic = models.ForeignKey(Topic,
#     on_delete=models.CASCADE,)
#     name = models.CharField(max_length = 264,unique = True)
#     url = models.URLField(unique=True)

# class AccessRecord(models.Model):
#     name = models.ForeignKey(Webpage,
#     on_delete=models.CASCADE,)
#     date = models.DateField()

# def __str__(self):
#     return str(self.date)


class Hostels(models.Model):

    HOSTEL_TYPE_CHOICES = [
        ('G', 'Gents'),
        ('L', 'Ladies'),
    ]

    hostel_name = models.CharField(max_length=255)
    hostel_address = models.TextField()
    hostel_contact_no = models.TextField()
    hostel_rent = models.IntegerField()
    mess_fees = models.IntegerField(null=True, default=0)
    hostel_type = models.CharField(max_length=2, choices=HOSTEL_TYPE_CHOICES)
    location_url = models.URLField(unique=True)
    hostel_image1 = models.ImageField(
        upload_to='hostels_images', null=True, default='hostels_images/1.jpg')
    hostel_image2 = models.ImageField(
        upload_to='hostels_images', null=True, default='hostels_images/1.jpg')
    hostel_image3 = models.ImageField(
        upload_to='hostels_images', null=True, default='hostels_images/1.jpg')
    hostel_image4 = models.ImageField(
        upload_to='hostels_images', null=True, default='hostels_images/1.jpg')
    hostel_image5 = models.ImageField(
        upload_to='hostels_images', null=True, default='hostels_images/1.jpg')

    def __str__(self):
        return str(self.hostel_name)
